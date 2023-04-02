import io
import os
from sunau import AUDIO_FILE_MAGIC
from google.cloud import speech_v1p1beta1 as speech
from google.cloud.speech_v1p1beta1 import enums

# Set up Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/credentials.json"

# Set up speech recognition client
client = speech.SpeechClient()

# Set up transcription request
config = speech.types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code='en-US',
)
audio = speech.types.RecognitionAudio(content=AUDIO_FILE_MAGIC.read())

# Perform transcription
response = client.recognize(config=config, audio=audio)

# Print transcribed text
for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))
