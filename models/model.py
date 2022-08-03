import os
from typing import List
import openai
import argparse
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input
    print(user_input)

    if validate_length(user_input):
        branding_result = generate_branding_snippet(user_input)
        keyword_result = generate_keywords(user_input)
        print(branding_result)
        print(keyword_result)
    else:
        raise ValueError("Input is too long")


def generate_branding_snippet(prompt: str):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    enriched_prompt = f'Generate branding snippet for {prompt}'

    response = openai.Completion.create(
        model="text-davinci-002", prompt=enriched_prompt, temperature=0, max_tokens=32)
    print(enriched_prompt)

    branding_text = response["choices"][0]["text"]
    branding_text = branding_text.strip()
    last_char = branding_text[-1]

    if last_char not in [".", "!", "?"]:
        branding_text += "..."

    print(f"Branding: {branding_text}")

    return branding_text


MAX_INPUT_LENGTH = 20


def validate_length(prompt: str) -> bool:
    return len(prompt) <= MAX_INPUT_LENGTH


def generate_keywords(prompt: str) -> List[str]:
    openai.api_key = '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'

    enriched_prompt = f'Generate related keywprd brandings for {prompt}'

    response = openai.Completion.create(
        model="text-davinci-002", prompt=enriched_prompt, temperature=0, max_tokens=32)

    keywords_text = response["choices"][0]["text"]
    keywords_text = keywords_text.strip()
    keywords_array = re.split(",|\n|;|-", keywords_text)
    keywords_array = [k.lower().strip() for k in keywords_array]
    keywords_array = [k for k in keywords_array if len(k) > 0]

    print(f"Keywords: {keywords_array}")
    return keywords_array


if __name__ == "__main__":
    main()
