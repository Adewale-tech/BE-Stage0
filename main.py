from fastapi import FastAPI
import requests
from datetime import datetime, timezone

app = FastAPI()

@app.get("/me")
def get_profile():
    try:
        # Fetch random cat fact from external API
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        cat_fact = response.json().get("fact", "Cats are awesome!")
    except Exception as e:
        cat_fact = "Unable to fetch cat fact at the moment."

    # Build response
    profile_data = {
        "status": "success",
        "user": {
            "email": "waliyullahadewale30@gmail.com",
            "name": "Osman Waliyullah",
            "stack": "Python/FastAPI"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

@app.get("/")
def read_root():
    return {"message": "Welcome! Your FastAPI app is running successfully 🚀"}

@app.get("/hello")
def hello():
    return {
  "status": "success",
  "user": {
    "email": "waliyullahadewale30@gmail.com",
    "name": "Osman Waliyullah",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-16T13:32:45.218Z",
  "fact": "Cats sleep for 70% of their lives."
}