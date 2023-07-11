from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix="/basicauth",
                   tags=["basicauth"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    Password: str


user_db = {
    "aamontess": {
        "username": "aamoontees",
        "full_name": "Andres Montes",
        "email": "aamonteess@gmail.com",
        "disabled": False,
        "Password": "123456"
    },
    "claris": {
        "username": "clarisa",
        "full_name": "Clara Isabel",
        "email": "clarisa@gmail.com",
        "disabled": False,
        "Password": "1234"
    },
    "pepito": {
        "username": "pepin",
        "full_name": "Pepe Palotes",
        "email": "pepinpalotes@gmail.com",
        "disabled": False,
        "Password": "1234"
    },
}


def search_user_db(username: str):
    if username in user_db:
        return UserDB(**user_db[username])


def search_user(username: str):
    if username in user_db:
        return User(**user_db[username])


async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=401, detail="No estas autorizado para esta accion")
        
    if user.disabled:
        raise HTTPException(
            status_code=401, detail="Usuario inactivo")
    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = user_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = search_user_db(form.username)
    if not form.password == user.Password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

    return {"access_token": user.username, "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
