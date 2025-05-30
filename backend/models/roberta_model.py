from transformers import pipeline

# Load your fine-tuned model from the local directory
classifier = pipeline(
    "text-classification",
    model="./models/model_output/checkpoint-634",
    tokenizer="./models/model_output/checkpoint-634"
)


def get_verdict(text):
    result = classifier(text)[0]
    label = result['label']
    score = result['score']
    verdict = "REAL" if label == "LABEL_1" else "FAKE"
    return {"verdict": verdict, "confidence": score}
