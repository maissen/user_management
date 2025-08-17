from fastapi import APIRouter, HTTPException
from ..db.connect_to_postgres import create_connection

router = APIRouter()

@router.get("/")
def test():
    conn = create_connection()
    if conn:
        conn.close()
        return {"status": "success", "message": "postgres is connected successfully"}
    else:
        raise HTTPException(status_code=500, detail="failed to connect to postgres")

