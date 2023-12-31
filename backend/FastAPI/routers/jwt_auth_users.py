from fastapi import APIRouter, Depends, HTTPException, status,FastAPI
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt,JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

router = APIRouter()


oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

algorithm = "HS256"
secret = "8f5babc6adacca2d6b0dc1cc2a774793ef8673f83ad83640474fd3a535d37a08"

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "yasiel": {
        "username": "yasiel",
        "full_name": "Brais Moure",
        "email": "braismoure@mourede.com",
        "disabled": False,
        "password": "$2a$12$SNyCIbgWnZwv3ssiWWCRxeG387P3T/mAVSWqSSoIHGlqjHQEtsFZu"
    },
    "mouredev2": {
        "username": "mouredev2",
        "full_name": "Brais Moure 2",
        "email": "braismoure2@mourede.com",
        "disabled": True,
        "password": "$2a$12$1FSotKeoai78UrLHX80HDOziLA2VcM8e1ZRKCvUDQjoxYcwl6eyO6"
    }
}

def search_user_db(username: str) -> UserDB:
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str) ->User:
    if username in users_db:
        return User(**users_db[username])
    
exception =  HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="las credenciales  son incorectas"
        )
async def oaut_user(token: str= Depends(oauth2))->User:
    try:
        username = jwt.decode(token,secret,algorithms=[algorithm]).get("sub")
        if username is  None:
           raise exception
            
    except JWTError : 
       raise exception
        
    return search_user(username)


async def current_user(user: User= Depends(oaut_user)) ->User:    
        
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")
    return user



@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):    
    user= search_user_db(form.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
     
    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    
    tokes_epiration_time = datetime.utcnow() + timedelta(minutes=60)
    token_user = {"sub":user.username,"exp":tokes_epiration_time}

    return {"access_token": jwt.encode(token_user,secret,algorithm=algorithm,), "token_type": "bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user))-> User:
    return user