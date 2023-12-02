import requests
import json

# url= "https://api.artic.edu/api/v1/artworks?limit=3"
# url1="https://www.google.com/"
# reques = requests.get(url1)
# print(reques)

# if reques.status_code == 200:
#   #print(reques.content)
#   reques_json = reques.json()["data"]
#   for art in reques_json:
#      print(f"{art['id']} {art['api_link']} ")

# else: print("estatus_couse != 200")



# file = open("google.com",'wb')
# file.write(reques.content)
# file.close()

#-------------------
# def howmany_pokemon(url="https://pokeapi.co/api/v2/pokemon", offset: int = 0  , limit: int = 20):
    
#     arg = {'offset': offset ,'limit': limit}
#     respose = requests.get(url,params= arg)
#     peyload = respose.json()['results']
   
#     for pokemon in peyload:
#       print(pokemon)
    
#     next_offset  = input("desea ver proxima pagian (Y/N)").lower()

#     if next_offset == "y":
#        howmany_pokemon(offset=offset+20)

#     elif next_offset == "n":
#        print("fin de la busqeuda")

#     else: print("Error en la entrada")       

# howmany_pokemon()


#-----------------


### pendiente
# url = "https://api.github.com"

# session = requests.session()
# session.auth = ('willito85@gmail.com','Sitioty85githubbk')
# response = session.get(url)
# if response.ok:
#     print(response.json())

# else: print(response.status_code)





##api with python with oauth##

# client_id = "ba068cc927b8e9b58667"
# client_secrets = "2ec3a0142c8019397638d519d3aef3c63fe8a71a"
# url = "https://github.com/login/oauth/access_token"
# code = "be9069c0d4889bc4dd67"
# header={'Accept': 'application/json'}
# load = {'client_id':client_id,'client_secret':client_secrets,'code':code}
# # https://github.com/login/oauth/authorize?client_id=ba068cc927b8e9b58667&scope=repo
# access_token_valor = "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"


# response = requests.post(url, json=load, headers=header)

# if response.status_code== 200:
#     respnse_json = response.json()
#     access_token = respnse_json["token_type"]
#     print(access_token)
    

# url_2 = "https://github.com/api/v3/user"

# # "Authorization: Bearer OAUTH-TOKEN"

# response_2 = requests.post(url, json=load, headers=header)



# def parameter(url):
#      return list(i.split('=')[1]  for i in url.split('?')[1].split('&'))


# print (parameter("https://retosdeprogramacion.com?year=2023&challenge=casa&offset=2&client_id=55&limit=2034"))




# from pydantic import BaseModel
# from fastapi import FastAPI,HTTPException,status

# app = FastAPI(responses={419 :{"mensage":"no se pudo crear el usuario"}})

# class Users(BaseModel):
#     id: int
#     name: str
#     url: str
#     age: int

# users_list = [Users(id=1,name="Pedro",url="www.sitioty.com",age=50),
#               Users(id=2,name="yanisey",url="www.yanilacubana.com",age=45),
#               Users(id=3,name="marta",url="www.martalamasfurte.com",age=95)]

# # http://127.0.0.1:8000/user
# @app.get("/users/",)

# async def usersjson():
#     return users_list


# # http://127.0.0.1:8000/user/2
# @app.get("/user/{id}")
# async def read_item(id: int):
#           return sears_user(id)

   

# # http://127.0.0.1:8000/userquery/?id=2
# @app.get("/user/")
# async def read_items(id: int): 
#           try:          
#             return sears_user(id)
#           except:
#                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="!AAAA")



# @app.post("/user/",response_model=Users,status_code=201)
# async def add_user(user: Users):
#      if type(sears_user(user.id)) == Users:
#        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="error el usuarios ya existe") 
#      else:
#         users_list.append(user)
#         return users_list[-1]
    


# @app.put("/user/",status_code=202)
# async def update_user(user:Users):
#      found= False

#      for index, user_save in enumerate(users_list):
#           if user.id == user_save.id:
#                users_list[index] = user
#                found = True
#                return users_list[index]

#      if not found:
#        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED,detail=("error usuario no actualizado"))    

# @app.delete("/user/{id}")
# async def delete_user(id:int):
#     found= False

#     for index, user_save in enumerate(users_list):
#           if id == user_save.id:
#                del users_list[index]
#                found = True
               
#     if not found:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="error usuario no se a eliminado")    




# def sears_user(id:int)->Users:
#     user= filter(lambda user: user.id== id, users_list)
#     try:
#         return list(user)[0]
#     except:
#         return  {"error" : "no hay mas usuarios"}
    

# from datetime import datetime,timedelta


# time = timedelta(minutes=5)
# print(time)

# timenow2 = datetime.utcnow()+ time
# print(timenow2)
# timenow = datetime.now()
# print(timenow)


# from enum import Enum

# from fastapi import FastAPI


# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"


# app = FastAPI()


# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": f"{ModelName.lenet}"}
    

#     return {"model_name": model_name, "message": "Have some residuals"}


# from fastapi import FastAPI

# app = FastAPI()

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]



# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
#     user_id: int, item_id: str, q: str | None = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# from fastapi import FastAPI
# from pydantic import BaseModel


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# app = FastAPI()


# @app.post("/items/")
# async def create_item(item: Item):
#     return item


# from fastapi import FastAPI
# from pydantic import BaseModel


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# app = FastAPI()


# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.model_dump()}



#  Crea una función que reciba un número decimal y lo trasforme a Octal
#  y Hexadecimal.
#  No está permitido usar funciones propias del lenguaje de programación que
#  realicen esas operaciones directamente..

# import math 
# def converter_in_octa_and_hexa(decimal):         
#     rest = []  
#     string= str()  
#     print (hex(decimal))  
#     print(oct(decimal))
#     while(True):
#        if int(decimal//8) != 0:          
#          rest.insert(0,decimal%8)
#          decimal = int(decimal/8)
#        else: break  
#     rest.insert(0,decimal)  
     
#     for i in rest:   
#        string += str(i)
#     string = int(string)
#     print (string)
   
    
# converter_in_octa_and_hexa(500)

#  Crea una función que dibuje una escalera según su número de escalones.
#   - Si el número es positivo, será ascendente de izquiera a derecha.
#   - Si el número es negativo, será descendente de izquiera a derecha.
#   - Si el número es cero, se dibujarán dos guiones bajos (__).
  
#   Ejemplo: 4
#        _8
#      _|6     
#    _|4
#  _|2 
#_|

#    _
#  _|
#_|

#  _
#_|

#
#_
# |_
#   |_
#
#


# def ladder(steps:int):
#     no_step="__"
#     white_space=""
#     step_up = "|"
#     step_down= "_"
             
#     if steps>0:
#         for spase in range(steps*2):
#             white_space+=" "
#         print(white_space+step_down)
#         white_space=""             
#         while (steps>0):
#             for spase in range((steps*2)-2):
#                 white_space+=" "
#             print(white_space+step_down+step_up)
#             white_space=""
#             steps-=1            
#     elif steps<0:
#         print(step_down)
#         rang = 1
#         while (steps<0):
#          white_space = ""
#          for spase in range(rang):
#                 white_space+=" "
#          rang+=2
#          print(white_space+step_up+step_down)
#          steps+=1        
#     else:
#      print(no_step)  

# ladder(1)





# from datetime import datetime, timedelta
# from typing import Annotated

# from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from pydantic import BaseModel

# # to get a string like this run:
# # openssl rand -hex 32
# SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30


# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
#         "disabled": False,
#     }
# }


# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData(BaseModel):
#     username: str | None = None


# class User(BaseModel):
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     disabled: bool | None = None


# class UserInDB(User):
#     hashed_password: str


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto",)

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# app = FastAPI()


# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)


# def get_password_hash(password):
#     return pwd_context.hash(password)


# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)


# def authenticate_user(fake_db, username: str, password: str):
#     user = get_user(fake_db, username)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user


# def create_access_token(data: dict, expires_delta: timedelta | None = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


# async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     user = get_user(fake_users_db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user


# async def get_current_active_user(
#     current_user: Annotated[User, Depends(get_current_user)]
# ):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user


# @app.post("/token", response_model=Token)
# async def login_for_access_token(
#     form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
# ):
#     user = authenticate_user(fake_users_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}


# @app.get("/users/me/", response_model=User)
# async def read_users_me(
#     current_user: Annotated[User, Depends(get_current_active_user)]
# ):
#     return current_user


# @app.get("/users/me/items/")
# async def read_own_items(
#     current_user: Annotated[User, Depends(get_current_active_user)]
# ):
#     return [{"item_id": "Foo", "owner": current_user.username}]


# var = -2
# print(-var)






# from fastapi import FastAPI
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel


# class Item(BaseModel):
#     id: str
#     value: str


# class Message(BaseModel):
#     message: str


# app = FastAPI()


# @app.get("/items/{item_id}", response_model=Item, responses={404: {"model": Message}})
# async def read_item(item_id: str):
#     if item_id == "foo":
#         return {"id": "foo", "value": "there goes my hero"}
#     return JSONResponse(status_code=404, content={"message": "Item not found"})




### Reto # 19  ###

#  Crea un programa que analice texto y obtenga:
#  - Número total de palabras.
#  - Longitud media de las palabras.
#  - Número de oraciones del texto (cada vez que aparecen un punto).
#  - Encuentre la palabra más larga.
 
#  Todo esto utilizando un único bucle.

# def new_func():
#     def analiza_text(dir:str):
#         with open(dir,"r") as file:
#             words = file.read().split()
#             numero_total_palabra = 0
#             longitud_media_de_palabra= 0
#             numero_de_oraciones = 0
#             palabra_más_larga = ""
#             for word in words:
#                 numero_total_palabra+=1
#                 if "."== word[-1]:
#                     numero_de_oraciones+=1
#                     word=word[:-1]
#                 longitud_media_de_palabra += len(word)
#                 if len(word) > len(palabra_más_larga):
#                     palabra_más_larga = word
#             longitud_media_de_palabra /= len(words)
#             file.close()
#             print(f"{numero_total_palabra}  {longitud_media_de_palabra} {numero_de_oraciones}  {palabra_más_larga}")



#     analiza_text("C:\Temp\temp\python_code\New_Text_Document.txt")

# new_func()


# from datetime import datetime, timedelta
# from typing import Annotated

# from fastapi import Depends, FastAPI, HTTPException, Security, status
# from fastapi.security import (
#     OAuth2PasswordBearer,
#     OAuth2PasswordRequestForm,
#     SecurityScopes,
# )
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from pydantic import BaseModel, ValidationError

# # to get a string like this run:
# # openssl rand -hex 32
# SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30


# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "$2a$12$1YkGclMnWTyIBX4QH.2NBOJOzom9qVwwhx.AAmZxzCzDlEFV7npYi",
#         "disabled": False,
#     },
#     "alice": {
#         "username": "alice",
#         "full_name": "Alice Chains",
#         "email": "alicechains@example.com",
#         "hashed_password": "$2b$12$gSvqqUPvlXP2tfVFaWK1Be7DlH.PKZbv5H8KnzzVgXXbVxpva.pFm",
#         "disabled": True,
#     },
# }


# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData(BaseModel):
#     username: str | None = None
#     scopes: list[str] = []


# class User(BaseModel):
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     disabled: bool | None = None


# class UserInDB(User):
#     hashed_password: str


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth2_scheme = OAuth2PasswordBearer(
#     tokenUrl="token",
#     scopes={"me": "Read information about the current user.", "items": "Read items."},
# )

# app = FastAPI()


# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)


# def get_password_hash(password):
#     return pwd_context.hash(password)


# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)


# def authenticate_user(fake_db, username: str, password: str):
#     user = get_user(fake_db, username)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user


# def create_access_token(data: dict, expires_delta: timedelta | None = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


# async def get_current_user(
#     security_scopes: SecurityScopes, token: Annotated[str, Depends(oauth2_scheme)]
# ):
#     if security_scopes.scopes:
#         authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
#     else:
#         authenticate_value = "Bearer"
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": authenticate_value},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_scopes = payload.get("scopes", [])
#         token_data = TokenData(scopes=token_scopes, username=username)
#     except (JWTError, ValidationError):
#         raise credentials_exception
#     user = get_user(fake_users_db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     for scope in security_scopes.scopes:
#         if scope not in token_data.scopes:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="Not enough permissions",
#                 headers={"WWW-Authenticate": authenticate_value},
#             )
#     return user


# async def get_current_active_user(
#     current_user: Annotated[User, Security(get_current_user, scopes=["me"])]
# ):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user


# @app.post("/token", response_model=Token)
# async def login_for_access_token(
#     form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
# ):
#     user = authenticate_user(fake_users_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username, "scopes": form_data.scopes},
#         expires_delta=access_token_expires,
#     )
#     return {"access_token": access_token, "token_type": "bearer"}


# @app.get("/users/me/", response_model=User)
# async def read_users_me(
#     current_user: Annotated[User, Depends(get_current_active_user)]
# ):
#     return current_user


# @app.get("/users/me/items/")
# async def read_own_items(
#     current_user: Annotated[User, Security(get_current_active_user, scopes=["items"])]
# ):
#     return [{"item_id": "Foo", "owner": current_user.username}]


# @app.get("/status/")
# async def read_system_status(current_user: Annotated[User, Depends(get_current_user)]):
#     return {"status": "ok"}



from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})


