from fastapi import APIRouter
from app.api.v1.endpoints import auth

# ایجاد روتر مرکزی نسخه 1
api_router = APIRouter()

# اضافه کردن روتر احراز هویت با پیش‌وند /auth
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])