<<<<<<< HEAD
# backend/api/analyze.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from analysis.analyzer import analyze_text  

router = APIRouter()

class NewsInput(BaseModel):
    text: str

@router.post("/analyze")
def analyze_news(data: NewsInput):
    try:
        return analyze_text(data.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
=======
# backend/api/analyze.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from analysis.analyzer import analyze_text  

router = APIRouter()

class NewsInput(BaseModel):
    text: str

@router.post("/analyze")
def analyze_news(data: NewsInput):
    try:
        return analyze_text(data.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
>>>>>>> 6ac8cb5b9277ce7b32d914c3ec38b1778756be9a
