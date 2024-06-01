import json
from transformers import pipeline

def sentiment_analyzer(text_to_analyze):
    nlp = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", revision="main")
    result = nlp(text_to_analyze)
    label = result[0]['label']
    score = result[0]['score']
    return {'label': label, 'score': score}

def handler(event, context):
    text_to_analyze = event['queryStringParameters']['textToAnalyze']
    response = sentiment_analyzer(text_to_analyze)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps(response),
    }
