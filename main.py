# main.py
from fastapi import FastAPI
from datetime import datetime
import requests

app = FastAPI()

@app.get("/me")
def get_profile():
    try:
        # Fetch random cat fact
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        if response.status_code == 200:
            cat_fact = response.json().get("fact", "Cats are amazing creatures!")
        else:
            cat_fact = "Could not fetch a cat fact at the moment."
    except Exception:
        cat_fact = "Cat fact service unavailable."

    return {
        "status": "success",
        "user": {
            "email": "waliyullahadewale30@gmail.com",   # your email
            "name": "Osman Waliyullah Adewale",         # your full name
            "stack": "Python/FastAPI"                   # your backend stack
        },
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "fact": cat_fact
    }
