from typing import Optional, List
from sqlalchemy.orm import Session

import fastapi
from fastapi import Path, Query, Depends, HTTPException

from schemas.user import User, UserCreate
from api.service.users import get_user_by_id, get_user_by_email, get_users, create_user
from db.db_setup import get_db

router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def fetch_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_users(db, skip, limit)


@router.post("/users", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail=f'user with email {user.email} already exists in db')

    return create_user(db, user)


@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    existing_user = get_user_by_id(db, user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail=f'user with id {user_id} not found in db')
    return existing_user
