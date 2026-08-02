from pydantic import BaseModel


class TextRequest(BaseModel):

    text: str



class SentimentResponse(BaseModel):

    sentiment: str

    confidence: float
