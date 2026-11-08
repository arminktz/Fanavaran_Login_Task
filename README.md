# سامانه احراز هویت و مدیریت کاربران (FastAPI + Vue 3)

پروژه کامل احراز هویت و مدیریت حساب کاربری پیاده‌سازی شده با معماری لایه‌ای (Layered Architecture) در بک‌اند و فرانت‌اند مدرن با Vue 3، Pinia و Tailwind CSS.

## 🏗 معماری پروژه (Layered Architecture)

بخش بک‌اند پروژه بر اساس **معماری لایه‌ای ۴ گانه** پیاده‌سازی شده است تا تفکیک وظایف (Separation of Concerns)، نگهداری آسان و قابلیت تست‌پذیری تضمین شود:

```
       ┌────────────────────────┐
       │   API / Router Layer   │  ──> دریافت درخواست‌های HTTP و پاسخ‌دهی
       └───────────┬────────────┘
                   │
       ┌───────────▼────────────┐
       │     Service Layer      │  ──> منطق تجاری، هش رمز، مدیریت توکن JWT
       └───────────┬────────────┘
                   │
       ┌───────────▼────────────┐
       │    Repository Layer    │  ──> تعامل با دیتابیس و اجرای کوئری‌ها
       └───────────┬────────────┘
                   │
       ┌───────────▼────────────┐
       │  Models & Database     │  ──> مدل‌های SQLAlchemy 2.0 (SQLite)
       └────────────────────────┘
```

## 🛠 تکنولوژی‌های استفاده‌شده

### بک‌اند (Backend)

* **فریم‌ورک:** FastAPI
* **دیتابیس:** SQLite به همراه Async SQLAlchemy 2.0
* **مدیریت مایگریشن:** Alembic
* **امنیت و احراز هویت:** JWT (python-jose) + Bcrypt

### فرانت‌اند (Frontend)

* **فریم‌ورک / ابزار ساخت:** Vue 3 (Composition API) + Vite
* **مدیریت وضعیت (State Management):** Pinia
* **استایل‌دهی:** Tailwind CSS v4 (طراحی واکنش‌گرا و راست‌چین / RTL)
* **ارتباط با API:** Axios

## 📁 ساختار پوشه‌ها و فایل‌ها

```
Fanavaran_Login_Task/
├── backend/
│   ├── alembic/              # اسکریپت‌های مدیریت تغییرات و مایگریشن دیتابیس
│   ├── app/
│   │   ├── api/              # لایه API (Endpoints & Routers)
│   │   │   └── v1/
│   │   │       ├── endpoints/
│   │   │       │   └── auth.py
│   │   │       └── router.py
│   │   ├── core/             # تنظیمات امنیتی (JWT, Password Hashing) و Config
│   │   ├── db/               # نشست‌های Async دیتابیس
│   │   ├── models/           # مدل‌های SQLAlchemy
│   │   ├── repositories/     # لایه Repository (Data Access)
│   │   ├── schemas/          # مدل‌های اعتبارسنجی Pydantic
│   │   └── services/         # لایه Service (Business Logic)
│   ├── main.py               # نقطه ورود سرور FastAPI
│   ├── alembic.ini
│   └── requirements.txt
│
└── frontend/
    ├── src/
    │   ├── stores/           # Pinia Auth Store (مدیریت توکن و کاربر)
    │   ├── views/            # صفحات اصلی (AuthView, HomeView)
    │   ├── App.vue
    │   ├── main.js
    │   └── style.css
    ├── vite.config.js
    └── package.json
```

## 🚀 راهنمای راه‌اندازی و اجرای پروژه

### ۱. اجرای بک‌اند (FastAPI)

۱. وارد پوشه بک‌اند شوید:

```bash
cd backend
```

۲. محیط مجازی پایتون را بسازید و فعال کنید:

```bash
python -m venv venv
# در ویندوز:
.\venv\Scripts\activate
```

۳. کتابخانه‌ها را نصب کنید:

```bash
pip install -r requirements.txt
```

۴. دیتابیس را به آخرین مایگریشن به‌روزرسانی کنید:

```bash
alembic upgrade head
```

۵. سرور توسعه بک‌اند را اجرا کنید:

```bash
fastapi dev main.py
# یا:
uvicorn main:app --reload
```

* **مستندات تعاملی Swagger:** `http://127.0.0.1:8000/docs`

### ۲. اجرای فرانت‌اند (Vue 3)

۱. در ترمینال جدید وارد پوشه فرانت‌اند شوید:

```bash
cd frontend
```

۲. پکیج‌ها را نصب کنید:

```bash
npm install
```

۳. سرور توسعه فرانت‌اند را روشن کنید:

```bash
npm run dev
```

* **آدرس فرانت‌اند:** `http://localhost:5173`

## 📌 ای‌پوینت‌های سیستم (API Endpoints)

| متد | مسیر (Endpoint) | توضیحات | احراز هویت |
| :--- | :--- | :--- | :---: |
| `POST` | `/api/v1/auth/register` | ثبت‌نام کاربر جدید | ❌ |
| `POST` | `/api/v1/auth/login` | ورود و دریافت توکن JWT | ❌ |
| `GET` | `/api/v1/auth/me` | دریافت اطلاعات کاربر فعال | ✅ |
