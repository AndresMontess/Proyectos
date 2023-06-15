from fastapi import FastAPI

app = FastAPI()

#Nos dice que podemos llamar a algo que contenga una /
#Siempre que llamemos a un servidor tenemos que usar solicitudes asincrona




@app.get("/")
async def root():
    return "Hola FastAPI!"

@app.get("/url")
async def root():
    return { "Url_api": "https://andres.com/python"   }

