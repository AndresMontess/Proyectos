from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET =  "201d573bd7d1344d3a3bfce1550b69102fd11be3db6d379508b6cccc58ea230b" 


router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt =  CryptContext(schemes=["bcrypt"])

exception = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str
'''
NOTA: a python y al json por lo que se ve les gusta tener sintaxis en misnucula por ello cuando llamabas a Password no funcionaba y cuando llamas por el body a password si funciona
es esquisito para la escritura de codigo por lo cual debes ser preciso y no poner mayus a no ser que sea necesario para el proyecto
'''

users_db = {
    "montes": {
        "username": "montes",
        "full_name": "Andres Montes",
        "email": "aamonteess@gmail.com",
        "disabled": False,
        "password": "$2a$12$B2Gq.Dps1WYf2t57eiIKjO4DXC3IUMUXISJF62bSRiFfqMdOI2Xa6"
    },
    "claris": {
        "username": "clarisa",
        "full_name": "Clara Isabel",
        "email": "clarisa@gmail.com",
        "disabled": False,
        "password": "$2a$12$SduE7dE.i3/ygwd0Kol8bOFvEABaoOOlC8JsCSr6wpwB4zl5STU4S"
    },
    "pepito": {
        "username": "pepin",
        "full_name": "Pepe Palotes",
        "email": "pepinpalotes@gmail.com",
        "disabled": False,
        "password": "$2a$12$SduE7dE.i3/ygwd0Kol8bOFvEABaoOOlC8JsCSr6wpwB4zl5STU67"
    },
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def auth_user(token : str = Depends(oauth2)):
    
    try:
        username = jwt.decode(token,SECRET,algorithms=[ALGORITM]).get("sub")
        if username is None:
            raise exception
            
    except JWTError:
                raise exception
    
    return search_user(username)
        

async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=401, detail="Usuario inactivo")
    return user



@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):

    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

    access_token = {"sub": user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}
    
    return {"access_token": jwt.encode(access_token, SECRET ,ALGORITM), "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user