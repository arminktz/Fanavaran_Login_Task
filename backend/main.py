from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import api_router  # ایمپورت روتر مرکزی

app = FastAPI(
    title="Auth System API",
    description="Backend API with FastAPI, SQLAlchemy Async, Alembic and JWT",
    version="1.0.0"
)

# CORS Middleware Configuration
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# متصل کردن روتر اصلی با پیش‌وند api/v1
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to Auth System Backend!"}