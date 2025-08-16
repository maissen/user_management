from fastapi import HTTPException
from ..services import user_service
from typing import Dict, Any

async def get_all_users() -> Dict[str, Any]:
    """Get all users - handles HTTP exceptions only"""
    try:
        users = await user_service.get_all_users()
        return {"status": "success", "data": users}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

async def get_user_by_id(user_id: int) -> Dict[str, Any]:
    """Get user by ID - handles HTTP exceptions only"""
    if user_id <= 0:
        raise HTTPException(status_code=400, detail="User ID must be positive")
    
    try:
        user = await user_service.get_user_by_id(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return {"status": "success", "data": user}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

async def create_user(name: str, email: str) -> Dict[str, Any]:
    """Create new user - handles HTTP exceptions only"""
    if not name or not email:
        raise HTTPException(status_code=400, detail="Name and email are required")
    
    if "@" not in email:
        raise HTTPException(status_code=400, detail="Invalid email format")
    
    try:
        user = await user_service.create_user(name, email)
        return {"status": "success", "data": user, "message": "User created successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


async def delte_user_by_id(user_id: int) -> Dict[str, Any]:

    if user_id is None or user_id < 0:
        raise HTTPException(status_code=500, detail="Invalid user id")
    
    user = await user_service.delete_user_by_id(user_id=user_id)
    return {"status": "success", "message": "user is deleted successfully"}
