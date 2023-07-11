from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

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

@router.get("/usersjson")
async def usersjson():
    return [{"name": "Andrés", "surname":"Montes", "url":"En proceso", "age": 19},
            {"name": "Pepe", "surname":"Pilotes", "url":"pilotes.com", "age": 24},
            {"name": "Clara", "surname":"Perec", "url":"Claraperec.com", "age": 56}]

@router.get("/users")
async def users():
    return users_list

@router.get("/usera/{id}")
async def user(id: int):
    users = filter(lambda user:user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error" : "No se ha encontrado el usuario"}
    

@router.post("/user/", response_model=User, status_code=201)
async def user(userq: User):
    if type(search_user(userq.id)) == User:
        raise HTTPException(status_code=204,detail="Usuario ya existe")
    else:
        users_list.append(userq)
        return userq
        
    
@router.put("/user/")
async def user(user: User):
    found = False
    for index , saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    
    if not found:
        return {"error" : "No se ha encontrado el usuario"}
    else:
        return user
   
   
@router.delete("/user/{id}")
async def user(id: int):
       for index , saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
                      



def search_user(id: int):
    users = filter(lambda user:user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error" : "No se ha encontrado el usuario"}
