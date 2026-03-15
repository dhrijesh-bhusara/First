from groq import Groq
from dotenv import load_dotenv
import os
import shutil

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_fix(ticket, file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    prompt = f"""
You are a senior backend engineer.

Bug report:
{ticket}

Below is a buggy file.

Fix the issue and return the COMPLETE corrected file.

File path:
{file_path}

Code:
{code}

Return only corrected code.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def apply_fix(file_path, fixed_code):

    backup = file_path + ".backup"

    if os.path.exists(backup):
        os.remove(backup)

    shutil.copy(file_path, backup)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(fixed_code)

    return backup