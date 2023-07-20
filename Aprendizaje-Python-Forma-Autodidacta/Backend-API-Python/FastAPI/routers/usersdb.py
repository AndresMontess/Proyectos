from fastapi import APIRouter, HTTPException
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import objectid

router = APIRouter()



users_list = []

@router.get("/db", response_model=list(User))
async def users():
    return users_schema(db_client.local.users.find())



@router.get("/db/{id}")
async def user(id: int):
    users = filter(lambda user:user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error" : "No se ha encontrado el usuario"}
    

@router.post("/db", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user_email(user.email)) == User:
       raise HTTPException(status_code=204,detail="Usuario ya existe")
    else:
        user_dict = dict(user) 
        del user_dict["id"]
    
        id = db_client.local.users.insert_one(user_dict).inserted_id
    
        new_user = user_schema(db_client.local.users.find_one({"_id" : id}))
    
        return User(**new_user)
        
    
@router.put("/db")
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
   
   
@router.delete("/db/{id}")
async def user(id: int):
       for index , saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
                      



def search_user_email(email: str):
    try:
         user = user_schema(db_client.local.users.find_one({"email" : email}))
         return user(**user)
    except:
        return {"error" : "No se ha encontrado el usuario"}
