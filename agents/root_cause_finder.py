from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_code(ticket, file_paths):

    code_context = ""

    for file in file_paths[:3]:   # limit to first 3 files

        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()

                code_context += f"\nFILE: {file}\n"
                code_context += content[:2000]   # limit size

        except:
            pass

    prompt = f"""
You are a senior backend engineer.

Incident ticket:
{ticket}

Analyze the following code snippets and determine:

1. Which file likely contains the bug
2. Root cause of the issue
3. Short explanation

Code snippets:
{code_context}

Return structured explanation.
"""

    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

    return response.choices[0].message.content