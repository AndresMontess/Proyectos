from fastapi import FastAPI
from routers import products, users, jwt_auth_users, basic_auth_users 

app = FastAPI()

app.include_router(products.router)
app.include_router(users.router)

app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
#Nos dice que podemos llamar a algo que contenga una /
#Siempre que llamemos a un servidor tenemos que usar solicitudes asincrona


@app.get("/")
async def root():
    return "Hola FastAPI!"

@app.get("/url")
async def url():
    return { "Url_api": "https://andres.com/python"   }

