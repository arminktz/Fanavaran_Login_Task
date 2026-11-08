# سامانه احراز هویت (FastAPI + Vue 3)

پروژه کامل احراز هویت کاربران (ثبت‌نام، ورود و داشبورد کاربری) پیاده‌سازی شده با معماری لایه‌ای (Layered Architecture) در بک‌اند و ترکیب Vue 3، Pinia و Tailwind CSS در فرانت‌اند.

---

## 🏗 معماری پروژه (Layered Architecture)

بخش بک‌اند پروژه بر اساس **معماری ۴ لایه‌ای** پیاده‌سازی شده تا تفکیک وظایف (Separation of Concerns) و قابلیت تست‌پذیری به حداکثر برسد:

```text
       ┌────────────────────────┐
       │   API / Router Layer   │  ──> دریافت درخواست‌های HTTP و پاسخ‌دهی
       └───────────┬────────────┘
                   │
       ┌───────────▼────────────┐
       │     Service Layer      │  ──> منطق تجاری، هش رمز، تولید توکن JWT
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

---

## 🛠 تکنولوژی‌های استفاده‌شده

### بک‌اند (Backend)
* **پایتون:** FastAPI
* **دیتابیس:** SQLite به همراه Async SQLAlchemy 2.0
* **مدیریت مایگریشن:** Alembic
* **امنیت و احراز هویت:** JWT (python-jose) + Bcrypt

### فرانت‌اند (Frontend)
* **فریم‌ورک:** Vue 3 (Composition API) + Vite
* **مدیریت وضعیت (State Management):** Pinia
* **استایل‌دهی:** Tailwind CSS v4 (طراحی راست‌چین / RTL)
* **ارتباط با API:** Axios

---

## 📁 ساختار پوشه‌ها

```text
Fanavaran_Login_Task/
├── backend/
│   ├── alembic/              # اسکریپت‌های مدیریت تغییرات دیتابیس
│   ├── app/
│   │   ├── api/              # لایه API (Endpoints & Routers)
│   │   ├── core/             # تنظیمات امنیتی (JWT, Password Hashing) و Config
│   │   ├── db/               # نشست‌های دیتابیس Async
│   │   ├── models/           # مدل‌های SQLAlchemy
│   │   ├── repositories/     # لایه Repository (Data Access)
│   │   ├── schemas/          # مدل‌های اعتبارسنجی Pydantic
│   │   └── services/         # لایه Service (Business Logic)
│   ├── main.py               # نقطه‌ی ورود FastAPI
│   └── alembic.ini
│
└── frontend/
    ├── src/
    │   ├── stores/           # Pinia Auth Store
    │   ├── views/            # صفحات اصلی (AuthView, HomeView)
    │   ├── App.vue
    │   └── main.js
    ├── vite.config.js
    └── package.json
```

---

## 🚀 راهنمای راه‌اندازی و اجرای پروژه

### ۱. اجرای بک‌اند (FastAPI)

۱. وارد پوشه بک‌اند شوید:
   ```bash
   cd backend
   ```

۲. محیط مجازی را بسازید و فعال کنید:
   ```bash
   python -m venv venv
   # روی ویندوز:
   .\venv\Scripts\activate
   ```

۳. کتابخانه‌های مورد نیاز را نصب کنید:
   ```bash
   pip install fastapi "uvicorn[standard]" sqlalchemy alembic python-jose[cryptography] bcrypt greenlet
   ```

۴. دیتابیس را به آخرین لایه مایگریشن ارتقا دهید:
   ```bash
   alembic upgrade head
   ```

۵. سرور بک‌اند را اجرا کنید:
   ```bash
   uvicorn main:app --reload
   ```
   * سرور روی `http://127.0.0.1:8000` اجرا خواهد شد.
   * مستندات ای‌پوینت‌ها (Swagger UI) در `http://127.0.0.1:8000/docs` قابل مشاهده است.

---

### ۲. اجرای فرانت‌اند (Vue 3)

۱. در ترمینال جدید وارد پوشه فرانت‌اند شوید:
   ```bash
   cd frontend
   ```

۲. پکیج‌های جاوااسکریپت را نصب کنید:
   ```bash
   npm install
   ```

۳. سرور فرانت‌اند را روشن کنید:
   ```bash
   npm run dev
   ```
   * فرانت‌اند روی `http://localhost:5173` در دسترس خواهد بود.

---

## 📌 ای‌پوینت‌های اصلی سیستم

| متد | ای‌پوینت | توضیحات | نیاز به توکن |
| :--- | :--- | :--- | :---: |
| `POST` | `/api/v1/auth/register` | ثبت‌نام کاربر جدید | ❌ |
| `POST` | `/api/v1/auth/login` | ورود و دریافت توکن JWT | ❌ |
| `GET` | `/api/v1/auth/me` | دریافت اطلاعات کاربر فعال | ✅ |