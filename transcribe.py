# transcribe.py
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def transcribe_audio(filename="input.wav"):
    try:
        print("🧠 Transcribing audio...")
        with open(filename, "rb") as f:
            transcript = openai.audio.transcriptions.create(
                model="whisper-1",
                file=f
            )
        print(f"📝 Transcript: {transcript.text}")
        return transcript.text
    except Exception as e:
        print(f"❌ Error transcribing audio: {e}")
        return None
