from fastapi import APIRouter, Request
from preprocessing.cleaner import clean_text
from analysis.analyzer import analyze_text
from database.mongo import save_result, get_recent_results
from socket_manager import sio  #  Not from main.py
from bson import ObjectId
from database.feedback import save_feedback
router = APIRouter()
@router.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    cleaned = clean_text(data["text"])
    result = analyze_text(cleaned)
    inserted = save_result(result)
    result["_id"] = str(inserted)  # Convert ObjectId to string
    await sio.emit("new_result", result)
    return result

@router.get("/recent-results")
def recent_results():
    return get_recent_results()
@router.post("/feedback")
async def submit_feedback(request: Request):
    data = await request.json()
    save_feedback(data)
    return {"message": "Feedback submitted successfully"}