from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Auth System"
    SECRET_KEY: str = "YOUR_SUPER_SECRET_KEY_CHANGE_THIS_IN_PROD"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day
    # تغییر آدرس دیتابیس به SQLite فایل‌محور
    DATABASE_URL: str = "sqlite+aiosqlite:///./auth.db"

    class Config:
        env_file = ".env"

settings = Settings()