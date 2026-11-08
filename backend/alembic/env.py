from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context

# این بخش تنظیمات را از فایل alembic.ini می‌خواند
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 1. ایمپورت کردن Base و تنظیمات برای شناخت مدل‌ها
from app.models.user import Base
from app.core.config import settings

# 2. اتصال متادیتای مدل‌ها به Alembic (اصلاح مقدار None به Base.metadata)
target_metadata = Base.metadata

# ست کردن داینامیک URL دیتابیس از فایل تنظیمات پروژه (.env / settings)
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode (Async Compatible)."""
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    import asyncio
    asyncio.run(run_migrations_online())