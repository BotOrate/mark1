import sounddevice as sd
from scipy.io.wavfile import write
import whisper

AUDIO_FILE = "user_input.wav"

def record_audio(filename, duration=5, samplerate=16000):
    print("Recording... Speak now!")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
    sd.wait()
    write(filename, samplerate, (audio * 32767).astype('int16'))
    print("Recording stopped.")

def transcribe_audio(filename):
    model = whisper.load_model("base.en")
    result = model.transcribe(filename)
    return result["text"].strip()

# Example usage:
# record_audio(AUDIO_FILE)
# query = transcribe_audio(AUDIO_FILE)
