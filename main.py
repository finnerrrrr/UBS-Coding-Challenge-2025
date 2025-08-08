import os
import re
import pickle
import numpy as np
import faiss
import google.generativeai as genai
import scrollvdb

# --------------------------
# 0) Configure Gemini Client
# --------------------------
genai.configure(api_key="AIzaSyAIzQ570Dr3ZOH81lqHqwIWg9LRYaJkuu0")  # Replace with your actual API key

INDEX_FILE = "scrolls.index"
META_FILE = "scrolls_meta.pkl"

# --------------------------
# 1) Embedding Function
# --------------------------
def get_embedding(text: str) -> np.ndarray:
    """Generate embeddings using Gemini's embedding model (Client API)."""
    resp = genai.embed_content(
        model="models/embedding-001",
        content=text
    )
    return np.array(resp["embedding"], dtype=np.float32)

# --------------------------
# 2) VDB Load/Save
# --------------------------
def load_vdb():
    """Load FAISS index and metadata (or initialize if missing)."""
    if os.path.exists(INDEX_FILE) and os.path.exists(META_FILE):
        index = faiss.read_index(INDEX_FILE)
        with open(META_FILE, "rb") as f:
            metadata = pickle.load(f)
    else:
        index = None
        metadata = []
    return index, metadata

def save_vdb(index, metadata):
    """Persist FAISS index and metadata to disk."""
    faiss.write_index(index, INDEX_FILE)
    with open(META_FILE, "wb") as f:
        pickle.dump(metadata, f)

# -----------------------------------------------------------------------------
# 4) Add Scroll to VDB (For continuous optimisation using output at runtime)
# -----------------------------------------------------------------------------
def add_scroll(valid_list, invalid_list, gree_expression):
    """Add a new scroll to FAISS index, skipping duplicates."""
    index, metadata = load_vdb()

    # Duplicate check
    new_scroll = {
        "valid": valid_list,
        "invalid": invalid_list,
        "gree_expression": gree_expression
    }
    if new_scroll in metadata:
        print("Scroll already exists in VDB. Skipping addition.")
        return  # Do not add duplicate

    # Add new scroll
    text_repr = f"VALID:{valid_list} INVALID:{invalid_list}"
    embedding = get_embedding(text_repr).reshape(1, -1)
    faiss.normalize_L2(embedding)

    index.add(embedding)
    metadata.append(new_scroll)
    save_vdb(index, metadata)
    print("Scroll added to VDB.")

# --------------------------
# 5) Retrieve Shots
# --------------------------
def retrieve_shots(valids, invalids, k=4):
    """Retrieve top-k similar scrolls from FAISS index."""
    index, metadata = load_vdb()
    if index is None or index.ntotal == 0:
        return ""  # No scrolls yet

    query_txt = f"VALID:{valids} INVALID:{invalids}"
    qemb = get_embedding(query_txt).reshape(1, -1)
    faiss.normalize_L2(qemb)
    _, I = index.search(qemb, k)

    shots = []
    for i in I[0]:
        scroll = metadata[i]
        shots.append(f"""VALID: {scroll['valid']}
INVALID: {scroll['invalid']}
GREE_EXPRESSION: {scroll['gree_expression']}""")
    return "\n\n".join(shots)

# ---------------------------------------------------------------------------
# 6) Validation Function for Auto-save of scrolls in generate_gree_expression
# ---------------------------------------------------------------------------

def validate_gree_expression(gree_expression, valid, invalid):
    if len(gree_expression) > 20:
            return False
    try:
        regex = re.compile(gree_expression)
    except re.error:
        return False
    return all(regex.fullmatch(s) for s in valid) and \
           all(not regex.fullmatch(s) for s in invalid)

# -------------------------------------------------------------------------------------
# 7) Generate Gree Expression with Gemini (With additional feedback loop)
# -------------------------------------------------------------------------------------

def generate_gree_expression(valids, invalids, max_attempts=10):
    # If length of valid or invalid lists is greater than 20, reject and return None
    if len(valids) > 20 or len(invalids) > 20:
        print("❌ Valid or invalid lists exceed maximum length of 20. Please reduce the number of examples.")
        return None
    """
    Generate a gree_expression using few-shot RAG with Gemini.
    Retries up to max_attempts times for failed attempts (With additional feedback for each failed attempt)
    """

    # Start off with no feedback, will accumulate feedback for failed attempts
    feedback = ""  

    for attempt in range(max_attempts):
        # Retrieve few-shot examples
        shots_text = retrieve_shots(valids, invalids)

        # Build prompt with feedback (if any)
        prompt = (
            "You’re a expert regex synthesizer. Given VALID & INVALID lists examples, output one regex (maximum length 20 characters) ONLY.\n\n"
            + "### Examples:\n"
            + shots_text
            + "### Now Synthesize:\n"
            + f"\n\nNOW:\nVALID: {valids}\nINVALID: {invalids}\n"
        )
        if feedback:
            prompt += f"Previous attempt failed: {feedback}\n"
        prompt += "REGEX:"

        # Generate gree_expression
        model = genai.GenerativeModel("gemini-2.5-flash")
        resp = model.generate_content(
            contents=prompt,
            generation_config={"temperature": 0}
        )

        try:
            if resp.parts:
                gree_expression = resp.text.strip()

                if validate_gree_expression(gree_expression, valids, invalids):
                    add_scroll(valids, invalids, gree_expression)
                    return gree_expression
                else:
                    feedback = (
                        f"'{gree_expression}' failed. Ensure it FULLY MATCHES all VALID strings and REJECTS all INVALID ones. "
                        "Use ^ and $ anchors. Avoid partial matches or overgeneral patterns."
                    )
            else:
                feedback = "Empty response from Gemini."

        except Exception as e:
            feedback = f"Error while processing model output: {str(e)}"

    print(f"❌ Failed to generate a valid gree_expression after {max_attempts} attempts.")
    return None

# --------------------------
# Example usage
# --------------------------

# Initialize FAISS index and metadata (Only upon starting up)
if not os.path.exists(INDEX_FILE) and not os.path.exists(META_FILE):
    docs = []
    for scroll in scrollvdb.SCROLLS:
        # Create text representation
        text = f"VALID:{scroll['valid']} INVALID:{scroll['invalid']}"
        # Get embedding
        embedding = get_embedding(text)
        docs.append({
            "embedding": embedding,
            "valid": scroll["valid"],
            "invalid": scroll["invalid"],
            "gree_expression": scroll["gree_expression"]
        })

    dimension = len(docs[0]["embedding"])
    index = faiss.IndexFlatIP(dimension)  # Inner product index

    # Normalize embeddings
    embeddings = np.stack([doc["embedding"] for doc in docs])
    faiss.normalize_L2(embeddings)
    index.add(embeddings)

    # Prepare metadata and save
    metadata = [
        {"valid": doc["valid"], "invalid": doc["invalid"], "gree_expression": doc["gree_expression"]}
        for doc in docs
    ]
    save_vdb(index, metadata)

# Testing
listofdics = [
        # {
        #     "valid": ["whaa at??!", "oh hell no!!!!!", " lol", "234 p"],
        #     "invalid": ["1223", "whatisit", "pl333", "f;/nsgafj"],
        #     "gree_expression": r"^.*\s.*$"
        # },
        # {
        #     "valid": ["ver1.0", "app2.3", "mod3.9", "block4.5"],
        #     "invalid": ["ver10", "app.3", "mod39", "block 4.5"],
        #     "gree_expression": r"^\w+\d\.\d$"
        # },
        # {
        #     "valid": ["lmfao", "lol", "l8908"],
        #     "invalid": ["bmfao", "a4o", "rpk", "18908"],
        #     "gree_expression": r"^[l]\w+$"
        # },
        # {
        #     "valid": ["haha", "1l1l", "xyxy", "z9z9", "hahahahahaha"],
        #     "invalid": ["123123", "hahah", "A+A+A+", "aabb"],
        #     "gree_expression": r"^(\w\w)\1+$"
        # },
        {
            "valid": ["gogogo", "world", "worororo"],
            "invalid": ["hey", "wait", "hullo world"],
            "gree_expression": r"^\S*o\S*$"
        }
    ]

for dic in listofdics:
    gree_expression_X = generate_gree_expression(dic["valid"], dic["invalid"])
    print("Generated Gree expression:", gree_expression_X) 