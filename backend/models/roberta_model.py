import os
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from pathlib import Path
import logging

class FakeNewsDetector:
    def __init__(self, model_path=None):
        if model_path is None:
            model_path = os.getenv("FAKE_NEWS_MODEL_PATH", "models/Fake-News-Bert-Detect")
        model_path = Path(model_path).resolve().as_posix()

        self.tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path, local_files_only=True)
        self.pipeline = pipeline(
            "text-classification",
            model=self.model,
            tokenizer=self.tokenizer,
            return_all_scores=True
        )

    def predict(self, text):
        try:
            scores = self.pipeline(text)[0]
            scores_dict = {item['label'].upper(): item['score'] for item in scores}
            label = max(scores, key=lambda x: x['score'])['label'].upper()
            confidence = scores_dict.get(label, 0.0)
            verdict = "REAL" if label == "REAL" else "FAKE"
            reason = "Content appears verifiable." if verdict == "REAL" else "Content appears unreliable."

            return {
                "verdict": verdict,
                "confidence": round(confidence, 4),
                "reason": reason,
                "source_type": "ml"
            }
        except Exception as e:
            logging.error(f"Model prediction failed: {str(e)}")
            return {
                "verdict": "UNKNOWN",
                "confidence": 0.0,
                "reason": "Model prediction failed.",
                "source_type": "ml"
            }
