from fastapi import FastAPI

from mongo_client import client

app = FastAPI()
app.state.mongo_client = client

@app.post("/login/", response_model=dict)
async def create_secret(phone: str) -> dict:
    return {"phone": phone}
