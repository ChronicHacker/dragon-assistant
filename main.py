# main.py
from wake_word import detect_wake_word
from record_audio import record_audio
from transcribe import transcribe_audio
from chat import ask_gpt
from speak import speak
import time
from datetime import datetime
import os
import subprocess

os.makedirs("logs", exist_ok=True)

def log_interaction(prompt, response):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"logs/{timestamp}.txt"
    with open(filename, "w") as f:
        f.write(f"Time: {timestamp}\n")
        f.write(f"You: {prompt}\n")
        f.write(f"Dragon: {response}\n")

def main():
    while True:
        print("\n🔉 Ready. Say 'Porcupine' to activate...")
        if detect_wake_word():
            print("🎤 Wake word detected! Starting voice recording...")

            if not record_audio():
                print("❌ Failed to record audio.")
                continue

            print("🧠 Transcribing...")
            prompt = transcribe_audio()
            if not prompt:
                print("⚠️ No speech detected or transcription failed.")
                continue

            print(f"📨 Prompt: {prompt}")

            cancel_keywords = ["cancel", "never mind", "nevermind", "stop", "scratch that"]
            if any(phrase in prompt.lower() for phrase in cancel_keywords):
                print("❌ Cancelled by voice command.")
                speak("Alright. Let me know if you need anything else.")
                continue

            subprocess.run(["aplay", "-D", "plughw:1,0", "thinking.wav"])

            response = ask_gpt(prompt)
            if not response:
                print("⚠️ GPT didn't return a response.")
                continue

            print(f"🤖 Response: {response}")
            log_interaction(prompt, response)
            speak(response)

        time.sleep(1)

if __name__ == "__main__":
    main()
