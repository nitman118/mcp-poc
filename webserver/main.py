from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="My Simple FastAPI")

class SumRequest(BaseModel):
    a: float
    b: float

@app.get("/ping")
async def ping():
    return {"status": "ok"}

@app.post("/sum")
async def sum_numbers(body: SumRequest):
    return {"sum": body.a + 2*body.b}