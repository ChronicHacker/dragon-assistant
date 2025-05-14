# chat.py
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(prompt):
    try:
        print("💬 Sending to GPT...")
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        reply = response.choices[0].message.content.strip()
        print(f"🤖 GPT says: {reply}")
        return reply
    except Exception as e:
        print(f"❌ GPT error: {e}")
        return None
