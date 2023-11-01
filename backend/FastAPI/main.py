from fastapi import FastAPI
from routers import product,users,basic_auth_users,jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles


app  = FastAPI()

#routers
app.include_router(users.router)
app.include_router(product.router)
#app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

#static resources
app.mount("/static",StaticFiles(directory="static"),name="static")


@app.get("/")
async def root():
    return {"Hello users!!"}

@app.get("/url")
async def url():
    return {"url":"https://github.com/ElValeroBK"}


## uvicorn main:app --reload
## stop server (ctrl+C)
# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc
#### python -m uvicorn main:app --reload