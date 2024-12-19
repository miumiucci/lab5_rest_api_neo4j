from fastapi import HTTPException

API_TOKEN = "749f233e4ff64dda08c3132a8766656c"

def verify_token(token: str):
    if token != API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")
    return token
