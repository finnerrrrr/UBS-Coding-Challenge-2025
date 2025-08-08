# Gree Expression Synthesizer (RAG + LLM)
## What this does
Given two lists—VALID and INVALID strings—main.py produces a single regex (≤ 20 chars) that fully matches every VALID and rejects every INVALID.

It uses a hybrid:

RAG (FAISS): retrieve the most similar solved “scrolls” as few-shot examples.

LLM (Gemini): synthesize a candidate regex from those shots.

Auto-validation & feedback: locally test; on failure, retry with concise feedback; on success, store the new scroll to improve future retrieval.

## Methods used
Vector retrieval: IndexFlatIP on L2-normalized embeddings (cosine similarity).

Few-shot prompting: inject retrieved VALID/INVALID/GREE_EXPRESSION trios.

Deterministic generation: temperature=0.

Validation: re.fullmatch must pass all valids and fail all invalids.

Continuous learning: successful solutions appended to the FAISS store.

## Files
main.py — all logic (embeddings, FAISS, prompting, validation, feedback loop).

scrollvdb.py — seed examples (SCROLLS) used to initialize the index on first run.

Generated on first run: scrolls.index, scrolls_meta.pkl.

## Setup
1) Install deps
bash
Copy
pip install google-generativeai faiss-cpu numpy
2) Configure API key (do not hardcode)
bash
Copy

#### macOS/Linux
export GEMINI_API_KEY="YOUR_KEY"

#### Windows PowerShell
$env:GEMINI_API_KEY="YOUR_KEY"

## Running

bash

Copy

python main.py

On first run, FAISS is seeded from scrollvdb.SCROLLS and index files are created.

### To test custom cases, call:

python

Copy

gree = generate_gree_expression(valids, invalids, max_attempts=20)

print("Generated:", gree)


## How it works (quick)

Embed query: VALID:[...] INVALID:[...] → models/embedding-001.

Retrieve shots: top-k nearest scrolls from FAISS.

Prompt LLM: instruction + “### Examples” + “### Now Synthesize … REGEX:”.

Validate: compile and check anchors & full-match behavior.

Feedback loop: on failure, retry with brief, explicit feedback (≤ max_attempts).

Persist: on success, append new scroll to FAISS + metadata.

## Troubleshooting

Empty/failed LLM response: check GEMINI_API_KEY and network; re-run.

FAISS empty/corrupt: delete scrolls.index / scrolls_meta.pkl to reseed.

Regex fails validation: the loop retries with feedback until success or max_attempts is hit.


