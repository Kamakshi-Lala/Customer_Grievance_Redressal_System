from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from llm.infer import classify_with_rag

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ComplaintInput(BaseModel):
    complaint: str

@app.post("/classify")
def classify(data: dict):
    try:
        result = classify_with_rag(data['complaint'])
        return {"result": result} 
    except Exception as e:
        return {"error": str(e)}