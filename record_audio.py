# record_audio.py
import sounddevice as sd
import scipy.io.wavfile as wav

def record_audio(filename="input.wav", duration=5):
    try:
        fs = 44100
        print("🎙 Recording for 5 seconds...")
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()
        wav.write(filename, fs, recording)
        print(f"✅ Saved recording to: {filename}")
        return True
    except Exception as e:
        print(f"❌ Error recording audio: {e}")
        return False
