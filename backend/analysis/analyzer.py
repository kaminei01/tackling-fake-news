import os
import json
from models.roberta_model import FakeNewsDetector
from analysis.manual_override import manual_fake_check
from analysis.web_verifier import fetch_news_sources

# Initialize detector
detector = FakeNewsDetector()

# Load known real/fake claims
file_path = os.path.join(os.path.dirname(__file__), "known_facts.json")
try:
    with open(file_path, "r", encoding="utf-8") as f:
        known_facts = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    known_facts = []

TRUSTED_DOMAINS = [
    "bbc.com", "reuters.com", "ndtv.com", "timesofindia.indiatimes.com",
    "theguardian.com", "cnn.com", "nytimes.com", "time.com",
    "forbes.com", "foxnews.com", "cnbc.com", "indiatoday.in", "nasa.gov"
]

SATIRE_DOMAINS = [
    "theonion.com", "babylonbee.com", "waterfordwhispersnews.com",
    "clickhole.com", "thedailymash.co.uk", "newsbiscuit.com"
]

ABSURD_PHRASES = [
    "flying pigs", "talking bananas", "cows voting", "cats ruling the world",
    "cats control world governments", "pizza cures all diseases", "unicorn discovered",
    "chocolate-powered car", "aliens endorse bitcoin", "ice cream stops climate change",
    "oxygen ban", "government bans oxygen", "cows apply for id", "banana president",
    "eiffel tower will be relocated", "eiffel tower moved", "moon made of cheese",
    "government to ban gravity", "earth is flat and proved by scientists", "drinking bleach", "ingesting bleach", "bleach cure", 
    "disinfectant as medicine", "bleach approved as cure",
    "bleach approved for covid", "bleach approved for coronavirus",
]

KNOWN_REAL_CLAIMS = [
    "india successfully lands chandrayaan-3 near moon's south pole",
    "nasa’s perseverance rover discovers organic molecules on mars",
    "world health organization declares covid-19 no longer a global emergency"
]

def dynamic_reason(verdict, confidence):
    if verdict == "FAKE":
        if confidence > 0.9:
            return "Highly confident in detecting fake content due to misleading language patterns."
        elif confidence > 0.7:
            return "Likely fake; content shows signs of manipulation or exaggeration."
        else:
            return "Possibly fake, but evidence is limited or unclear."
    else:  # Real
        if confidence > 0.9:
            return "Strong indications of authenticity from credible patterns."
        elif confidence > 0.7:
            return "Seems real but cross-verification is suggested."
        else:
            return "Likely real, but confidence is moderate."

def is_absurd(text):
    text_lower = text.lower()
    return any(phrase in text_lower for phrase in ABSURD_PHRASES)

def has_satire_source(sources):
    for s in sources:
        if any(domain in s.get("url", "") for domain in SATIRE_DOMAINS):
            return True
    return False

def trusted_sources(sources):
    return [s for s in sources if any(domain in s.get("url", "") for domain in TRUSTED_DOMAINS)]

def analyze_text(text, debug=False):
    normalized_text = text.strip().lower()

    # 1. Check known facts
    for fact in known_facts:
        if normalized_text == fact.get("text", "").strip().lower():
            return {
                "verdict": fact.get("verdict", "UNKNOWN"),
                "confidence": round(float(fact.get("confidence", 0.0)), 4),
                "reason": fact.get("reason", ""),
                "source_type": fact.get("source_type", ""),
                "tags": fact.get("tags", []),
                "sources": fact.get("sources", [])
            }

    # 2. Check for absurd/impossible claims
    if is_absurd(normalized_text):
        return {
            "verdict": "FAKE",
            "confidence": 1.0,
            "reason": "Claim contains absurd or impossible content.",
            "source_type": "absurdity-check",
            "tags": ["absurd"],
            "sources": []
        }

    # 3. Check for known real claims
    if normalized_text in KNOWN_REAL_CLAIMS:
        return {
            "verdict": "REAL",
            "confidence": 1.0,
            "reason": "This claim is verified in multiple trusted sources.",
            "source_type": "known-real",
            "tags": ["verified", "trusted"],
            "sources": []
        }

    # 4. Manual override
    if manual_fake_check(text):
        return {
            "verdict": "FAKE",
            "confidence": 1.0,
            "reason": "Flagged as fake based on manual rule.",
            "source_type": "manual-check",
            "tags": ["flagged"],
            "sources": []
        }

    # 5. Web verification
    try:
        sources = fetch_news_sources(text)
    except Exception as e:
        sources = []
        if debug:
            print(f"Web source fetch failed: {e}")

    if has_satire_source(sources):
        return {
            "verdict": "FAKE",
            "confidence": 1.0,
            "reason": "Claim appears only on satire/parody websites.",
            "source_type": "satire-check",
            "tags": ["satire"],
            "sources": sources
        }

    trusted = trusted_sources(sources)
    trusted_count = len(trusted)
    total_count = len(sources)

    # 6. Trusted sources logic
    if trusted_count >= 3:
        confidence = min(1.0, trusted_count / (total_count or 1))
        return {
            "verdict": "REAL",
            "confidence": round(confidence, 4),
            "reason": "Verified by three or more credible sources from the web.",
            "source_type": "web-search",
            "tags": ["auto-verified", "trusted-sources"],
            "sources": trusted
        }
    elif trusted_count in (1, 2):
        confidence = min(0.5, trusted_count / 4)
        return {
            "verdict": "POSSIBLY_REAL",
            "confidence": round(confidence, 4),
            "reason": "Verified by only one or two credible sources from the web.",
            "source_type": "web-search-partial",
            "tags": ["possibly-real", "trusted-sources"],
            "sources": trusted
        }
    elif total_count > 0:
        confidence = min(0.3, total_count / 10)
        return {
            "verdict": "UNKNOWN",
            "confidence": round(confidence, 4),
            "reason": "Found only untrusted or unrelated sources.",
            "source_type": "web-search-untrusted",
            "tags": ["web-sources"],
            "sources": sources
        }

    # 7. ML model fallback
    result = detector.predict(text)
    score = float(result.get("confidence", 0.0))
    verdict = result.get("verdict", "UNKNOWN")
    if score < 0.3:
        verdict = "UNCERTAIN"
    return {
        "verdict": verdict,
        "confidence": round(score, 4),
        "reason": result.get("reason", dynamic_reason(verdict, score)),
        "source_type": result.get("source_type", "ml"),
        "tags": ["auto-verified"],
        "sources": sources or []
    }
