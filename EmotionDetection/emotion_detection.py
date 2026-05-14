# URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
# Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
# Input json: { "raw_document": { "text": text_to_analyze } }
import requests 
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    data = response.json()

    emotion_data = data['emotionPredictions'][0]['emotion']

    dominant_emotion = max(emotion_data, key=emotion_data.get)

    formatted_output = {
        'anger': emotion_data.get('anger', 0),
        'disgust': emotion_data.get('disgust', 0),
        'fear': emotion_data.get('fear', 0),
        'joy': emotion_data.get('joy', 0),
        'sadness': emotion_data.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }
    return formatted_output
