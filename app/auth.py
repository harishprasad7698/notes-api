from passlib.context import CryptContext
import os
from dotenv import load_dotenv
from datetime import datetime,timedelta,timezone
import jwt
from jwt.exceptions import InvalidTokenError
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException,status,Depends
from sqlalchemy.orm import Session
from app import database,models



load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
 


pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")

def hash_password(password : str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password :str ,hashed_password:str)-> bool:
    return pwd_context.verify(plain_password,hashed_password)

def create_access_token(data:dict):
    to_encode =data.copy()
    expiry = datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expiry})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload_dict = jwt.decode(token,key=SECRET_KEY,algorithms=[ALGORITHM])
        username =payload_dict.get("sub")
    except InvalidTokenError:
        raise credentials_exception
    if username is None:
        raise credentials_exception
    user = db.query(models.User).filter(models.User.username==username).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="usernamenot found")
    return user

    
        