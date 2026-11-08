# مستندات جامع پروژه سامانه احراز هویت (Modular Monolith)

این داکیومنت شامل شرح کامل معماری، نحوه ساختاردهی، راهنمای راه‌اندازی و پیاده‌سازی پروژه یکپارچه احراز هویت با استفاده از **FastAPI** در بک‌اند و **Vue 3** در فرانت‌اند می‌باشد.

---

## 🛠 فناوری‌های استفاده شده (Tech Stack)

### بک‌اند (Backend)
- **فریم‌ورک:** FastAPI
- **دیتابیس:** SQLite (با Async SQLAlchemy 2.0)
- **مایگریشن:** Alembic
- **امنیت:** JWT (JSON Web Tokens) و bcrypt جهت هش‌سازی رمز عبور
- **معماری:** Layered Architecture (معماری لایه‌ای)

### فرانت‌اند (Frontend)
- **فریم‌ورک/ابزار ساخت:** Vue 3 (Composition API) + Vite
- **مدیریت وضعیت:** Pinia
- **استایل‌دهی:** Tailwind CSS v4 (RTL)
- **ارتباط با API:** Axios

---

## 📁 ساختار پروژه (Project Directory Structure)

```text
Fanavaran_Login_Task/
├── backend/
│   ├── alembic/                  # اسکریپت‌های مدیریت تغییرات دیتابیس
│   │   ├── versions/
│   │   └── env.py
│   ├── app/
│   │   ├── api/                  # لایه Controller / Router
│   │   │   └── v1/
│   │   │       ├── endpoints/
│   │   │       │   └── auth.py
│   │   │       └── router.py
│   │   ├── core/                 # تنظیمات اصلی و امنیت
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── db/                   # لایه دیتابیس و نشست‌ها
│   │   │   ├── base.py
│   │   │   └── session.py
│   │   ├── models/               # مدل‌های SQLAlchemy
│   │   │   └── user.py
│   │   ├── repositories/         # لایه Data Access (Repository)
│   │   │   └── user_repository.py
│   │   ├── schemas/              # Pydantic Schemas
│   │   │   └── user.py
│   │   └── services/             # لایه Business Logic
│   │       └── auth_service.py
│   ├── alembic.ini
│   ├── main.py
│   └── .env
└── frontend/
    ├── src/
    │   ├── assets/
    │   ├── components/
    │   ├── stores/
    │   │   └── auth.js           # Pinia Store
    │   ├── views/
    │   │   ├── AuthView.vue      # کامپوننت ورود / ثبت‌نام
    │   │   └── HomeView.vue      # داشبورد اصلی کاربر
    │   ├── App.vue
    │   ├── main.js
    │   └── style.css
    ├── index.html
    ├── vite.config.js
    └── package.json
```

---

## ⚙️ راهنمای راه‌اندازی و اجرا

### ۱. بخش بک‌اند (FastAPI)

#### ۱.۱. فعال‌سازی محیط مجازی و نصب وابستگی‌ها
```bash
cd backend
python -m venv venv
# فعال‌سازی در ویندوز:
.\venv\Scripts\activate

# نصب پکیج‌های ضروری
pip install fastapi "uvicorn[standard]" sqlalchemy alembic python-jose[cryptography] bcrypt greenlet
```

#### ۱.۲. اجرای مایگریشن‌های دیتابیس با Alembic
برای ایجاد و اعمال جداول دیتابیس:
```bash
# ایجاد فایل مایگریشن جدید
alembic revision --autogenerate -m "create users table"

# اعمال تغییرات روی دیتابیس
alembic upgrade head
```

#### ۱.۳. اجرای سرور توسعه
```bash
fastapi dev main.py
# یا استفاده از Uvicorn:
uvicorn main:app --reload
```
سرویس بک‌اند روی آدرس `http://127.0.0.1:8000` و مستندات Swagger روی `http://127.0.0.1:8000/docs` در دسترس خواهد بود.

---

### ۲. بخش فرانت‌اند (Vue 3 + Vite + Tailwind CSS v4)

#### ۲.۱. نصب وابستگی‌ها
```bash
cd frontend
npm install
npm install pinia vue-router axios tailwindcss @tailwindcss/vite
```

#### ۲.۲. کانفیگ Tailwind CSS v4 در Vite
در فایل `vite.config.js`:
```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    vue(),
    tailwindcss(),
  ],
})
```

و اضافه کردن کد زیر در `src/style.css`:
```css
@import "tailwindcss";
```

#### ۲.۳. اجرای سرور فرانت‌اند
```bash
npm run dev
```
برنامه فرانت‌اند روی آدرس `http://localhost:5173` اجرا می‌شود.

---

## 🔑 ای‌پوینت‌های اصلی سیستم (API Endpoints)

| متد | مسیر (Endpoint) | توضیحات | احراز هویت |
|---|---|---|---|
| `POST` | `/api/v1/auth/register` | ثبت‌نام کاربر جدید | ❌ ندارد |
| `POST` | `/api/v1/auth/login` | ورود کاربر و دریافت توکن JWT | ❌ ندارد |
| `GET` | `/api/v1/auth/me` | دریافت اطلاعات کاربر جاری | ✅ نیازمند Bearer Token |

---

## 🛡️ نکات مهم امنیتی و رفع چالش‌ها (Troubleshooting)

1. **سازگاری SQLAlchemy Async با Greenlet:**
   در صورت بروز خطای `ImportError: The SQLAlchemy asyncio module requires that the Python 'greenlet' library is installed` باید پکیج `greenlet` به طور مستقیم نصب شود.

2. **هش‌سازی رمز عبور با Bcrypt:**
   برای جلوگیری از خطاهای مربوط به نسخه `passlib` و محدودیت ۷۲ بایتی، تابع هش‌سازی رمز عبور به‌صورت مستقیم با پکیج `bcrypt` پیاده‌سازی شد:
   ```python
   def get_password_hash(password: str) -> str:
       pwd_bytes = password.encode('utf-8')
       salt = bcrypt.gensalt()
       return bcrypt.hashpw(pwd_bytes, salt).decode('utf-8')
   ```

3. **پشتیبانی CORS در فست‌آپی:**
   جهت برقرار ارتباط بدون خطا بین Vue (پورت 5173) و فست‌آپی (پورت 8000)، `CORSMiddleware` در فایل `main.py` تنظیم شده است.