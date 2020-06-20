from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import sys

client = speech_v1.SpeechClient()

storage_uri = sys.argv[1]
language_code = "en-US"
model = 'phone_call'
use_enhanced = True
enable_automatic_punctuation = True
config = {
    "language_code": language_code,
    "model": model,
    "use_enhanced": use_enhanced,
    "enable_automatic_punctuation": enable_automatic_punctuation,
}
audio = {"uri": storage_uri}

operation = client.long_running_recognize(config, audio)
print(operation.operation)
print(u"Waiting for operation to complete...")
response = operation.result()

print(response)
