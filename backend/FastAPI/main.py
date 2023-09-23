from fastapi import FastAPI

app  = FastAPI()

@app.get("/")

async def root():
    return {"Hello users!!"}

@app.get("/url")
async def url():
    return {"url":"https://ElValeroBK.com/python/yasiel"}


## uvicorn main:app --reload
## stop server (ctrl+C)
# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc