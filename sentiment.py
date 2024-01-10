from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis", "distilbert-base-uncased-finetuned-sst-2-english")
#sentiment_model = pipeline("sentiment-analysis", "Distilbert-base-uncased-emotion")

feeling = ["About regular"]

result = sentiment_model(feeling)

print(result)