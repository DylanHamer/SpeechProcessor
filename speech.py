import requests

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

def hypothosis():
    with open("speechFile.mp3") as speechFile:
        speechJSON["audio"]["content"] = speechFile.open()
        json = requests.post(apiURL, data=speechJSON).json
    return json["hypothosis"]

print(hypothosis())
    
