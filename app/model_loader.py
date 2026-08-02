from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"


tokenizer = None
model = None
labels = None


def load_model():
    global tokenizer, model, labels
    if tokenizer is None or model is None or labels is None:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
        labels = model.config.id2label
    return tokenizer, model, labels
