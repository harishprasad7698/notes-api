from fastapi import FastAPI,Depends,HTTPException,status
from pydantic import BaseModel,Field
from app.database import SessionLocal, engine
from app import models
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()
class Note(BaseModel):
    title:str = Field(min_length=1)
    content:str = Field(min_length=1)

@app.get("/")
def read_root():
    return {"message": "Welcome to my Notes API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/notes")
def create_notes(note:Note, db : Session = Depends(get_db)):
    new_note = models.Note(title = note.title, content = note.content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

@app.get("/notes")
def get_notes(db: Session = Depends(get_db)):
    return db.query(models.Note).all()

@app.get("/notes/{note_id}")
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404 , detail="not found")
    return note

@app.delete("/notes/{note_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id:int,db:Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404 , detail="not found")
    db.delete(note)
    db.commit()

@app.put("/notes/{note_id}")
def update_note(note_id :int, update_note:Note,db:Session = Depends(get_db)):
    existing_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if existing_note is None:
        raise HTTPException(status_code=404 , detail="not found")
    existing_note.title = update_note.title
    existing_note.content = update_note.content
    db.commit()
    db.refresh(existing_note)
    return existing_note
    
