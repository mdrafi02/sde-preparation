from fastapi import APIRouter,status

import app.data as data
from app.models import User, UserCreate

router = APIRouter(
         prefix="/users",
         tags=["Users"]
        )

@router.post("", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate) -> User:
    user_id = data.next_user_id
    new_user = User(id=user_id, name=user.name, email=user.email)

    data.users[user_id] = new_user
    data.next_user_id += 1

    return new_user

@router.get("", response_model=list[User])
def get_users() -> list[User]:
    return list(data.users.values())


