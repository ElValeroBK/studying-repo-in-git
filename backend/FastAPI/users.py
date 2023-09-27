from fastapi import FastAPI
from pydantic import BaseModel


app  = FastAPI()


class Users(BaseModel):
    id: int
    name: str
    lastname: str
    url: str
    age: int

users_list = [Users(id=1, name="Danay", lastname="Padron", url="https://fastapi.tiangolo.com/tutorial/body/", age=36),
              Users(id=2, name="Brais", lastname="Moure", url="https://moure.dev", age=35),
              Users(id=3, name="Moure", lastname="Dev", url="https://mouredev.com", age=35),
              Users(id=4, name="Brais", lastname="Dahlberg", url="https://haakon.com", age=33)]

#get
@app.get("/user/")

async def usersjson():
    return users_list

#get
#path   http://127.0.0.1:8000/users/2
@app.get("/user/{item_id}")

async def read_item(item_id: int):

    users= filter(lambda user: user.id== item_id, users_list)
    try:
        return list(users)[0]
    except:
        return  {"error" : "no hay mas usuarios"}

 #get   
 # query   http://127.0.0.1:8000/usersquery/?item_id=1 
@app.get("/userquery/")

async def read_item(item_id: int):
    return user_search(item_id)

    
    
   

#post
@app.post("/user/")
async def creat_user(user: Users):
    if type(user_search(user.id)) == Users:
         return {"error" : "el usuario ya existe"}        
    else:
         users_list.append(user)
       

#put
@app.put("/user/")
async def update_user(user:Users):
    found = False
    

    for indix,userpulled in  enumerate(users_list):
        if userpulled.id == user.id:
            if users_list[indix]== user:
                return {"error" : "no has echo ningun cambio en el usuario"} 
            else:
                 users_list[indix] = user
            found = True
    if not found:
        return {"error" : "no existe el usuario"} 
    
    return user
    
    
           

    
#delate
@app.delete("/user/{id}")
async def delate_user(id: int):

    found = False
    for indix,userpulled in  enumerate(users_list):
        if userpulled.id == id:
            del users_list[indix]
            found = True
    if not found:
        return {"error" : "no se a eliminadoe el usuario"} 





def user_search(id:int):        
    users= filter(lambda user: user.id== id, users_list)
    try:
        return list(users)[0]
    except:
        return  {"error" : "no hay mas usuarios"}
    

