from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Note(BaseModel):
    title:"str"
    content:"str"

@app.get("/")
def read_root():
    return {"message": "Welcome to my Notes API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/notes")
def create_notes(note:Note):
    return{"message":"note created","note":note}