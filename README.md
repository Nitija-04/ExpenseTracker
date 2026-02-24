📁 Project Structure
EXPENSETRACKER/
├── backend/
│   ├── __init__.py
│   ├── crud/
│   │   ├── __init__.py
│   │   └── crud.py
│   ├── data/
│   │   ├── __init__.py
│   │   └── database.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── models.py
│   └── schemas/
│       ├── __init__.py
│       └── schemas.py
├── .env
├── env.py
├── cruds.py
├── database.py
├── main.py
├── models.sql
├── requirements.txt
├── schema.sql
└── .gitignore

✨ Features
✅ User registration & JWT login
✅ Full CRUD for user expenses
✅ Supabase PostgreSQL database
✅ Clean FastAPI + Pydantic structure

🛠️ Tech Stack
| Category   | Technology            |
| ---------- | --------------------- |
| Framework  | FastAPI               |
| Database   | Supabase (PostgreSQL) |
| ORM        | SQLAlchemy            |
| Validation | Pydantic              |
| Auth       | JWT Tokens            |

🚀 Quick Start
1. Clone & Setup
    git clone https://github.com/yourusername/expensetracker.git
cd expensetracker
# Virtual environment
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt

2. Environment
    Create .env from your Supabase project:
    DATABASE_URL=postgresql+psycopg2://postgres:[YOUR-PASSWORD]@db.[YOUR-ID].supabase.co:5432/postgres
    SECRET_KEY=your-super-secret-key-change-this
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30

3. Run Server
    uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

🌐 Live at:
http://localhost:8000
Swagger: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

🗄️ Database Schema
Setup Options:
# 1. Supabase Dashboard (Recommended)
    # Copy models.sql → SQL Editor → Run
# 2. Local PostgreSQL
    psql $DATABASE_URL -f models.sql

Tables Overview
| Table    | Purpose                        |
| -------- | ------------------------------ |
| users    | User accounts & authentication |
| expenses | User expenses w/ owner linking |

Full schema: models.sql | Pydantic: backend/schemas/schemas.py

🔗 API Endpoints
| Method | Endpoint       | Description        | Auth |
| ------ | -------------- | ------------------ | ---- |
| POST   | /users/        | Register new user  | No   |
| POST   | /token         | Login → JWT token  | No   |
| GET    | /expenses/     | List user expenses | Yes  |
| POST   | /expenses/     | Create expense     | Yes  |
| PUT    | /expenses/{id} | Update expense     | Yes  |
| DELETE | /expenses/{id} | Delete expense     | Yes  |

🧪 Testing
    pip install pytest httpx
    pytest backend/tests/  # Add tests folder when ready

📚 Key Files
| File                | Purpose                      |
| ------------------- | ---------------------------- |
| backend/main.py     | FastAPI app entrypoint       |
| backend/database.py | DB connection & session      |
| backend/models/     | SQLAlchemy table definitions |
| backend/schemas/    | Pydantic input/output models |
| backend/crud/       | CRUD operations & logic      |
| models.sql          | Complete database schema     |

☁️ Deployment
Recommended: Render, Railway, Fly.io
    1. Push to GitHub
    2. Connect platform
    3. Add env vars: DATABASE_URL, SECRET_KEY
    4. Deploy!

Dockerfile:
    FROM python:3.11-slim
    WORKDIR /app
    COPY requirements.txt .
    RUN pip install -r requirements.txt
    COPY . .
    CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

🤝 Contributing
Fork repository

    git checkout -b feature/amazing-feature
    git commit -m "Add amazing feature"
    Push & submit PR

📄 License
    MIT License