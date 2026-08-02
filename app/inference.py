import torch

from app.model_loader import (
    tokenizer,
    model,
    labels
)


def predict_sentiment(text):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True
    )


    with torch.no_grad():

        outputs = model(**inputs)


    probabilities = torch.nn.functional.softmax(
        outputs.logits,
        dim=1
    )


    confidence, prediction = torch.max(
        probabilities,
        dim=1
    )


    sentiment = labels[prediction.item()]


    return {

        "sentiment": sentiment,

        "confidence": round(
            confidence.item(),
            2
        )
    }
