# wake_word.py
import pvporcupine
import sounddevice as sd
import struct
import os
from dotenv import load_dotenv

load_dotenv()
access_key = os.getenv("PORCUPINE_ACCESS_KEY")

def detect_wake_word():
    try:
        porcupine = pvporcupine.create(access_key=access_key, keywords=["porcupine"])
        def callback(indata, frames, time_info, status):
            pcm = struct.unpack_from("h" * len(indata), indata)
            if porcupine.process(pcm) >= 0:
                print("🦔 Wake word 'Porcupine' detected!")
                raise KeyboardInterrupt

        with sd.InputStream(channels=1, samplerate=porcupine.sample_rate, callback=callback,
                            blocksize=porcupine.frame_length, dtype='int16'):
            print("🎤 Listening for wake word... Say: 'Porcupine'")
            try:
                while True:
                    pass
            except KeyboardInterrupt:
                return True

    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    finally:
        if 'porcupine' in locals():
            porcupine.delete()
