import re
import google.generativeai as genai
    
API_KEY = "API KEY HERE"  # Replace with your actual API key

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")


def generate_gree_expression(valid_strings, invalid_strings, ):
    max_length=20
    max_attempts=20

    # Few-shot examples to guide the model
    few_shots = """
    Example 1:
    Valid: ["abc", "def"]
    Invalid: ["123", "456"]
    Regex: ^\D+$

    Example 2:
    Valid: ["abc-1", "bbb-1", "cde-1"]
    Invalid: ["abc1", "bbb1", "cde1"]
    Regex: ^.+-.+$

    Example 3:
    Valid: ["aaa", "abb", "acc"]
    Invalid: ["bbb", "bcc", "bca"]
    Regex: ^[a].+$

    Example 4:
    Valid: ["foo@abc.com", "bar@def.net"]
    Invalid: ["baz@abc", "qux.com"]
    Regex: ^\D+@\w+\.\w+$
    """

    # Core prompt
    base_prompt = f"""
    Generate a regex (≤{max_length} chars) that matches ALL valid strings
    and rejects ALL invalid strings. Always use ^ and $ anchors.
    Do NOT include explanations, only output the regex itself.

    Output format:
    - Plain regex syntax (e.g., ^\\D+$ should be output as ^\D+$)
    - DO NOT, I REPEAT DO NOT include extra escaping of backslashes
    {few_shots}

    Now solve:
    Valid: {valid_strings}
    Invalid: {invalid_strings}
    """

    for attempt in range(max_attempts):
        response = model.generate_content(base_prompt)
        regex = response.text.strip().split("\n")[0]

        # Validate regex
        try:
            compiled = re.compile(regex)
        except re.error:
            base_prompt += f"\nInvalid regex generated: {regex}. Try again."
            continue

        if (all(compiled.fullmatch(s) for s in valid_strings) and
            all(not compiled.fullmatch(s) for s in invalid_strings) and
            len(regex) <= max_length):
            return regex  # Success

        # Feedback loop
        base_prompt += f"\nRegex failed tests: {regex}. Improve it."

    return None

def validate_regex(pattern, valid, invalid):
    try:
        regex = re.compile(pattern)
    except re.error:
        return False
    return all(regex.fullmatch(s) for s in valid) and \
           all(not regex.fullmatch(s) for s in invalid)


print(generate_gree_expression(['abc', 'def'], ['123', '456']))
print(generate_gree_expression(['aaa', 'abb', 'acc'],['bbb', 'bcc', 'bca']))
print(generate_gree_expression(['abc1', 'bbb1', 'ccc1'], ['abc', 'bbb', 'ccc']))
print(generate_gree_expression(['abc-1', 'bbb-1', 'cde-1'], ['abc1', 'bbb1', 'cde1']))
print(generate_gree_expression(["foo@abc.com", "bar@def.net"], ["baz@abc", "qux.com"]))

print(generate_gree_expression(['lmfao', 'lol', 'l'], ['akm', 'bmfao', 'rpk']))