from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from analysis.analyzer import analyze_text  

router = APIRouter()

class NewsInput(BaseModel):
    text: str

@router.post("/analyze")
async def analyze_news(data: NewsInput):
    try:
        return analyze_text(data.text)
    except Exception as e:
        # You might want to log the error here instead of returning it to the client
        raise HTTPException(status_code=500, detail="Internal server error.")

