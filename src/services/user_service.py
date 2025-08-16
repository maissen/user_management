from typing import List, Dict, Any, Optional

# In-memory storage for demo purposes
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"},
    {"id": 3, "name": "Bob Johnson", "email": "bob@example.com"}
]
next_id = 4

async def get_all_users() -> List[Dict[str, Any]]:
    """Pure logic: return all users"""
    return users.copy()

async def get_user_by_id(user_id: int) -> Optional[Dict[str, Any]]:
    """Pure logic: find user by ID"""
    for user in users:
        if user["id"] == user_id:
            return user.copy()
    return None

async def create_user(name: str, email: str) -> Dict[str, Any]:
    """Pure logic: create new user"""
    global next_id
    
    # Check if email already exists
    existing_user = await get_user_by_email(email)
    if existing_user:
        raise ValueError("Email already exists")
    
    # Create new user
    new_user = {
        "id": next_id,
        "name": name.strip(),
        "email": email.strip().lower()
    }
    
    users.append(new_user)
    next_id += 1
    
    return new_user.copy()

async def get_user_by_email(email: str) -> Optional[Dict[str, Any]]:
    """Pure logic: find user by email"""
    email_lower = email.strip().lower()
    for user in users:
        if user["email"] == email_lower:
            return user.copy()
    return None