from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def parse_ticket(ticket_text):

    prompt = f"""
You are an AI software engineer.

Analyze this incident ticket and extract:

1. Error Type
2. Component
3. API Endpoint
4. Possible Cause
5. Severity

Ticket:
{ticket_text}

Return JSON.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content