import os
import requests
from dotenv import load_dotenv

# Explicitly load the .env file from the full path
env_path = os.path.join(
    "C:/Users/srava/OneDrive/Desktop/tackling-fake-news/backend/analysis/.env.txt"
)
load_dotenv(dotenv_path=env_path)

SERPAPI_KEY = os.getenv("SERPAPI_KEY")  # Now it will load correctly

TRUSTED_DOMAINS = [
    "bbc.com", "reuters.com", "ndtv.com", "timesofindia.indiatimes.com",
    "theguardian.com", "cnn.com", "nytimes.com", "time.com",
    "forbes.com", "foxnews.com", "cnbc.com", "indiatoday.in"
]

def fetch_news_sources(query, max_results=5, debug=False):
    if not SERPAPI_KEY:
        print("[Web Verifier] Error: SERPAPI_KEY not set or could not be loaded.")
        return []

    try:
        response = requests.get(
            "https://serpapi.com/search",
            params={
                "q": query,
                "api_key": SERPAPI_KEY,
                "engine": "google",
                "hl": "en",
                "num": max_results,
                "tbm": "nws"  # Search in news tab
            },
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        sources = []
        for result in data.get("news_results", []):
            sources.append({
                "title": result.get("title"),
                "url": result.get("link"),
                "source": result.get("source"),
                "description": result.get("snippet"),
                "relevance_reason": "Found via Google News search"
            })

        if debug:
            print("Fetched sources:", sources)
            trusted = [s for s in sources if any(domain in s["url"] for domain in TRUSTED_DOMAINS)]
            print("Trusted sources:", trusted)

        return sources

    except requests.RequestException as e:
        print(f"[Web Verifier] Request error: {e}")
        return []

    except Exception as e:
        print(f"[Web Verifier] Unexpected error: {e}")
        return []