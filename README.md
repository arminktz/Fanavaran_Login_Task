# 🔐 سامانه احراز هویت و مدیریت کاربران (FastAPI + Vue 3)

این پروژه یک سیستم کامل و امن احراز هویت کاربری است که با استفاده از **FastAPI** در بک‌اند و **Vue 3** در فرانت‌اند پیاده‌سازی شده است. بخش بک‌اند پروژه کاملاً از الگوی **معماری لایه‌ای (Layered Architecture)** پیروی می‌کند.

---

## 🏗️ معماری بک‌اند (Layered Architecture)

کد سمت بک‌اند به لایه‌های کاملاً مستقل تقسیم شده است تا تفکیک مسئولیت‌ها (Separation of Concerns)، نگهداری ساده‌تر و قابلیت تست‌پذیری تضمین شود:

```text
               ┌────────────────────────┐
               │   API / Router Layer   │  <-- دریافت درخواست‌ها و اعتبارسنجی اولیه
               └───────────┬────────────┘
                           │
               ┌───────────▼────────────┐
               │     Service Layer      │  <-- منطق تجاری (Business Logic) و JWT
               └───────────┬────────────┘
                           │
               ┌───────────▼────────────┐
               │    Repository Layer    │  <-- دسترسی به داده‌ها و کوئری‌های SQL
               └───────────┬────────────┘
                           │
               ┌───────────▼────────────┐
               │  Models & Schemas      │  <-- مدل‌های SQLAlchemy و Pydantic
               └────────────────────────┘
```

---

## 🛠️ تکنولوژی‌های استفاده‌شده

### 🔹 بک‌اند (Backend)
* **FastAPI**: فریم‌ورک آسنکرون و مدرن پایتون
* **SQLAlchemy 2.0 (Async)**: ارتباط غیرهمزمان با دیتابیس SQLite
* **Alembic**: مدیریت و اعمال مایگریشن‌های پایگاه داده
* **JWT & bcrypt**: هش‌سازی امن رمز عبور با `bcrypt` و احراز هویت بر پایه `PyJWT`/`python-jose`

### 🔸 فرانت‌اند (Frontend)
* **Vue 3 (Composition API)**: فریم‌ورک اصلی فرانت‌اند
* **Vite**: ابزار ساخت سریع
* **Pinia**: مدیریت State احراز هویت و توکن کاربر
* **Tailwind CSS v4**: طراحی مدرن، RTL و کامپوننت‌های واکنش‌گرا
* **Axios**: ارسال درخواست‌های HTTP به بک‌اند

---

## 📁 ساختار پوشه‌بندی پروژه

```text
Fanavaran_Login_Task/
├── backend/
│   ├── alembic/              # اسکریپت‌های مدیریت تغییرات دیتابیس
│   ├── app/
│   │   ├── api/              # لایه API و سرویس‌دهی اندپوینت‌ها
│   │   │   └── v1/
│   │   │       ├── endpoints/
│   │   │       │   └── auth.py
│   │   │       └── router.py
│   │   ├── core/             # تنظیمات امنیتی، توکن‌ها و هش کردن رمزها
│   │   ├── db/               # نشست آسنکرون دیتابیس
│   │   ├── models/           # مدل‌های SQLAlchemy
│   │   ├── repositories/     # لایه Repository (Data Access)
│   │   ├── schemas/          # مدل‌های Pydantic برای DTOها
│   │   └── services/         # لایه Service (Business Logic)
│   ├── main.py               # نقطه ورود اپلیکیشن FastAPI
│   └── alembic.ini
│
└── frontend/
    ├── src/
    │   ├── stores/           # مدیریت وضعیت کاربر (Pinia Store)
    │   ├── views/            # صفحات ورود، ثبت‌نام و داشبورد
    │   ├── App.vue
    │   └── style.css
    └── vite.config.js
```

---

## 🚀 راهنمای نصب و اجرا

### ۱. اجرای بک‌اند (Backend)

```bash
cd backend

# ۱. ایجاد و فعال‌سازی محیط مجازی
python -m venv venv
# Windows:
.\venv\Scripts\activate

# ۲. نصب کتابخانه‌ها
pip install -r requirements.txt

# ۳. بروزرسانی دیتابیس
alembic upgrade head

# ۴. اجرای سرور
fastapi dev main.py
```
📍 **مستندات Swagger:** `http://127.0.0.1:8000/docs`

---

### ۲. اجرای فرانت‌اند (Frontend)

```bash
cd frontend

# ۱. نصب پکیج‌ها
npm install

# ۲. اجرای برنامه
npm run dev
```
📍 **آدرس فرانت‌اند:** `http://localhost:5173`

---

## 🔑 اندپوینت‌های اصلی API

| متد | مسیر (Endpoint) | توضیحات | نیاز به توکن |
| :--- | :--- | :--- | :---: |
| `POST` | `/api/v1/auth/register` | ثبت‌نام کاربر جدید | ❌ |
| `POST` | `/api/v1/auth/login` | ورود و دریافت توکن JWT | ❌ |
| `GET` | `/api/v1/auth/me` | دریافت پروفایل کاربر فعلی | ✅ |