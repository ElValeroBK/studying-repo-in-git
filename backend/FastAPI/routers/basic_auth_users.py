# from fastapi import FastAPI,HTTPException,status,Depends
# from pydantic import BaseModel
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 

# class User(BaseModel):
#     username: str
#     fullname: str
#     email: str
#     disabled: bool

# class Userdb(User):
#     password: str

# app= FastAPI()


# users_db= {
#     "yasielbk":{
#         "username": "yasielbk",
#         "fullname":"yasie Valero",
#         "email": "yasielbk@valero.com",
#         "disabled": True,
#         "password": 12345678

#     },    
#     "yasielbk2":{
#         "username": "yasielbk2",
#         "fullname":"yasie Angulo",
#         "email": "yasielb2k@valero.com",
#         "disabled": False,
#         "password": "87654321"       
#     }
# }

# oauth2=OAuth2PasswordBearer(tokenUrl="login")


# def search_user_db(username:str):
#     if username in users_db:
#         return Userdb(**users_db[username])
    
# def search_user(username: str):
#     if username in users_db:
#         return User(**users_db[username])

    
# async def current_user(token: Depends(oauth2)):
#     user = search_user_db(token)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Credenciales de autenticación inválidas",
#             headers={"WWW-Authenticate": "Bearer"})
#     if user.disabled:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Usuario inactivo")
#     return user 






# @app.post("/login")
# async def auth(form: OAuth2PasswordRequestForm = Depends()): 
#     user_db= users_db.get(form.username)
#     if not user_db:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
#                             detail= "el usuario no se ha encontrado") 
    
#     user = search_user(form.username)
#     if not user.password == form.password:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
#                             detail= "el password no es correcto") 
#     return {"access_token": user.username,"token_type": "bearer"}


             

# @app.get("/users/me")
# async def me(user: User = Depends(current_user)):
#     return user


### Users API con autorización OAuth2 básica ###

from fastapi import APIRouter, Depends, HTTPException, status,FastAPI
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# router = APIRouter(prefix="/basicauth",
#                    tags=["basicauth"],
#                    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "braismoure@mourede.com",
        "disabled": False,
        "password": "123456"
    },
    "mouredev2": {
        "username": "mouredev2",
        "full_name": "Brais Moure 2",
        "email": "braismoure2@mourede.com",
        "disabled": True,
        "password": "654321"
    }
}


def search_user_db(username: str) -> UserDB:
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str) ->User:
    if username in users_db:
        return User(**users_db[username])


async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"})

    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")

    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
     
    if not users_db.get(form.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

    return {"access_token": user.username, "token_type": "bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user