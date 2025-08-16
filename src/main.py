from fastapi import FastAPI
from routes.user_routes import router as user_router

app = FastAPI(
    title="User Management API",
    description="A simple FastAPI app with layered architecture",
    version="1.0.0"
)

app.include_router(user_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)