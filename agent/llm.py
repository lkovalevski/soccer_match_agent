import os
from litellm import completion
from config import MODEL, MAX_TOKENS

def generate_response(messages):
    response = completion(
        model=MODEL,
        messages=messages,
        max_tokens=MAX_TOKENS
    )
    return response.choices[0].message.content