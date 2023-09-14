from fastapi import FastAPI
from pydantic import BaseModel


app  = FastAPI()


class Users(BaseModel):
    name: str
    lastname: str
    url: str
    age: int

users_list = [Users(name ="Danay",lastname ="Padron",url= "https://fastapi.tiangolo.com/tutorial/body/",age= 36)]




@app.get("/users")

async def usersmet():
    return users_list


