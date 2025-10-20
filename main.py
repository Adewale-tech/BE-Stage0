from fastapi import FastAPI
import requests
from datetime import datetime
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/me")
def get_profile():
    try:
        # Fetch a cat fact
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        data = response.json()
        cat_fact = data.get("fact", "Cats are mysterious creatures.")
    except Exception:
        cat_fact = "Could not fetch cat fact at the moment."

    profile = {
        "status": "success",
        "user": {
            "email": "waliyullahadewale30@gmail.com",
            "name": "Osman Waliyullah Adewale",
            "stack": "Python/FastAPI"
        },
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "fact": cat_fact
    }

    return JSONResponse(content=profile, media_type="application/json")

    return {
        "status": "success",
        "user": {
            "email": "waliyullahadewale30@gmail.com",
            "name": "Osman Waliyullah Adewale",
            "stack": "Python/FastAPI"
        },
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "fact": cat_fact
    }
