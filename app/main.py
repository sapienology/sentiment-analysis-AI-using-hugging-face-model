from fastapi import FastAPI, HTTPException


from app.schemas import (
    TextRequest,
    SentimentResponse
)


from app.inference import predict_sentiment


from app.utils import clean_text



app = FastAPI(

    title="Sentiment Analysis API",

    description="Hugging Face Transformer Sentiment API",

    version="1.0"

)



@app.get("/")
def home():

    return {

        "message":
        "Sentiment Analysis API is running"

    }



@app.get("/health")
def health():

    return {

        "status":"healthy"

    }



@app.post(
    "/predict",
    response_model=SentimentResponse
)

def predict(request: TextRequest):


    text = clean_text(request.text)


    if not text:

        raise HTTPException(

            status_code=400,

            detail="Text cannot be empty"

        )


    result = predict_sentiment(text)


    return result