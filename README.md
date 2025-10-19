# BE-Stage0 — Dynamic Profile API

## Description
A simple RESTful API that returns personal profile info and a random cat fact fetched dynamically from the Cat Facts API.

---

## 📍 Endpoint
**GET /me**

### Example Response
```json
{
  "status": "success",
  "user": {
    "email": "waliyullahadewale30@gmail.com",
    "name": "Osman Waliyullah",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-19T12:34:56.789Z",
  "fact": "Cats can jump up to six times their length."
}
