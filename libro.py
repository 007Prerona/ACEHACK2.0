from sunau import AUDIO_FILE_MAGIC
import librosa
audio, sr = librosa.load(AUDIO_FILE_MAGIC, sr=44100)
audio = librosa.effects.preemphasis(audio, coef=0.97)
audio = librosa.util.normalize(audio)