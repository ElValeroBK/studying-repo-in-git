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


from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}


