from fastapi import APIRouter
from controllers import user_controller

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
async def get_all_users():
    return await user_controller.get_all_users()

@router.get("/{user_id}")
async def get_user_by_id(user_id: int):
    return await user_controller.get_user_by_id(user_id)

@router.post("/")
async def create_user(name: str, email: str):
    return await user_controller.create_user(name, email)