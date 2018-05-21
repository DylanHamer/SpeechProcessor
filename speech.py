"""
VoiceProcessor
Wrapper for Google Speech API - Apparently the Google Cloud platform costs money so I have no idea if this works or not
By Dylan Hamer
"""

import requests
import base64

apiURL = "https://speech.googleapis.com/v1/speech:recognize"

speechJSON = {
  "audio": {
    "content":None
  },
  "config": {
    "enableAutomaticPunctuation":True,
    "encoding": "LINEAR16",
    "languageCode": "en-US",
    "model": "default"
  }
}

def hypothesis():
    with open("speech.mp3", "rb") as speechFile:
        encodedFile = base64.b64encode(speechFile.read())
        speechJSON["audio"]["content"] = encodedFile
        json = requests.post(apiURL, data=speechJSON).json()
    return json
