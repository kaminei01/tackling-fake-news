from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
MODEL_NAME = "roberta-base"  # Or use any available binary classifier

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)


# Ensure model is in eval mode
model.eval()

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Label mapping: 0 => REAL, 1 => FAKE (based on model docs)
label_map = {0: "REAL", 1: "FAKE"}

def get_verdict(text: str):
    # Tokenize input
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    inputs = {key: val.to(device) for key, val in inputs.items()}

    # Run model
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.softmax(logits, dim=1)
        confidence, pred_class = torch.max(probs, dim=1)

    # Return structured result
    return {
        "verdict": label_map[pred_class.item()],
        "confidence": round(confidence.item(), 4)
    }
