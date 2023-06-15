from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Orientado a objetos
#Entidad User
#BaseModel nos da la capacidad de crear una entidad, tiene un mecanismo comcreto que nos permite crear cosas
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1,name="Andrés",surname="Montes",url= "En proceso", age=19),
                 User(id=2,name="Pepe",surname="Pilotes",url="pilotes.com", age=24),
                 User(id=3,name="Clara",surname="Perec",url="Claraperec.com",age=56)]

@app.get("/usersJson")
async def usersJson():
    return [{"name": "Andrés", "surname":"Montes", "Url":"En proceso", "age": 19},
            {"name": "Pepe", "surname":"Pilotes", "Url":"pilotes.com", "age": 24},
            {"name": "Clara", "surname":"Perec", "Url":"Claraperec.com", "age": 56}]

@app.get("/Users")
async def Users():
    return users_list

@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user:user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error" : "No se ha encontrado el usuario"}
    
@app.get("/usera/")
async def user(id: int):
    users = filter(lambda user:user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error" : "No se ha encontrado el usuario"}