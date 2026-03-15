from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_test(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    prompt = f"""
You are a QA engineer.

Generate a unit test for this file.

File:
{file_path}

Code:
{code}

Return only the test code.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def save_test(file_path, test_code):

    test_file = file_path + ".test.js"

    with open(test_file, "w", encoding="utf-8") as f:
        f.write(test_code)

    return test_file