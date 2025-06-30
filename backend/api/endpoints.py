from fastapi import APIRouter, Request
from preprocessing.cleaner import clean_text
from analysis.analyzer import analyze_text
from database.mongo import save_result, get_recent_results
from socket_manager import sio
from database.feedback import save_feedback
import logging

router = APIRouter()
logger = logging.getLogger("uvicorn")

@router.post("/analyze")
async def analyze(request: Request):
    data = await request.json()

    if "text" not in data:
        return {"error": "Missing 'text' field in request."}

    logger.info(f"Received text for analysis: {data['text'][:100]}...")
    cleaned = clean_text(data["text"])
    result = analyze_text(cleaned)

    # Fallbacks for missing fields
    db_result = {
        "claim": data["text"],  # original input
        "verdict": result.get("verdict", "UNKNOWN"),
        "confidence": result.get("confidence", 0.0),
        "reason": result.get("reason", "Model prediction based on available data."),
        "source_type": result.get("source_type", "general"),
        "tags": result.get("tags", ["news"]),
        "sources": result.get("sources", [])
    }

    save_result(db_result)
    await sio.emit("new_result", db_result)

    return db_result

@router.get("/recent-results")
def recent_results():
    return get_recent_results()

@router.post("/feedback")
async def submit_feedback(request: Request):
    data = await request.json()
    save_feedback(data)
    logger.info(f"Feedback received: {data}")
    return {"message": "Feedback submitted successfully"}
