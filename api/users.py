from typing import Optional, List
import fastapi
from fastapi import Path, Query
from pydantic import BaseModel

router = fastapi.APIRouter()


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


users = [
    User(email='u1@', is_active=True, bio='u1 bio'),
    User(email='u2@', is_active=False, bio='u2 bio'),
    User(email='u3@', is_active=False, bio='u3 bio here'),
]


@router.get("/users", response_model=List[User])
async def get_users():
    return users


@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return user.email


@router.get("/users/{user_id}")
async def get_user(
        user_id: int = Path(..., description='user id is expected here'),
        q: str = Query(None, max_length=5)):
    return {"user": users[user_id], "q": q}
