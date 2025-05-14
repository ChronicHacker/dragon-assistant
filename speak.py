import os
import requests
import subprocess
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def speak(text):
    print("🗣 Speaking with OpenAI TTS...")

    url = "https://api.openai.com/v1/audio/speech"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "tts-1",
        "voice": "shimmer",  # You can also try: 'nova', 'echo', etc.
        "input": text
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code != 200:
            print(f"❌ TTS API error: {response.status_code}, {response.text}")
            return

        with open("speech.mp3", "wb") as f:
            f.write(response.content)

        # Convert to WAV for aplay
        subprocess.run([
            "ffmpeg", "-y", "-i", "speech.mp3", "-ar", "24000", "speech.wav"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Play it through your USB speaker (edit device as needed)
        subprocess.run(["aplay", "-D", "plughw:1,0", "speech.wav"])

    except Exception as e:
        print(f"❌ Error using OpenAI TTS: {e}")
