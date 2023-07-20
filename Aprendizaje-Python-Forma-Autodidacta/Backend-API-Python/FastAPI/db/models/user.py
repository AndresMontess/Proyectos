from pydantic import BaseModel

class User(BaseModel):
    id: str | None
    Username: str
    email: str 