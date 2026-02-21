# AI-Powered Customer Support System

An AI-powered customer support backend built using **FastAPI**.
This project simulates a mini helpdesk system like Zendesk and is designed to demonstrate real-world backend development skills.

---

## 🚀 Features

- User Authentication (Register & Login)
- Role-based access (Admin / Customer)
- Ticket Creation & Management
- Ticket Status & Priority Tracking
- REST APIs with FastAPI
- Interactive Swagger UI
- Cloud Deployment Ready

---

## 🛠 Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite (can be upgraded to PostgreSQL)
- Uvicorn

---

## 📁 Project Structure

```
ai-support-system/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database/
│   │   ├── db.py
│   │   └── models.py
│   ├── auth/
│   │   ├── router.py
│   │   └── schemas.py
│   ├── tickets/
│   │   ├── router.py
│   │   └── schemas.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ Run Locally

### 1️⃣ Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/ai-support-system.git
cd ai-support-system
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Server
```bash
uvicorn app.main:app --reload
```

Server will run at:
```
http://127.0.0.1:8000
```

---

## 📘 API Documentation

Swagger UI:
```
/docs
```

Example:
```
http://127.0.0.1:8000/docs
```

---

## ☁️ Deployment (Render)

**Build Command**
```bash
pip install -r requirements.txt
```

**Start Command**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

Render automatically redeploys on every GitHub push.

---

## ✅ Project Status

- ✔ Backend completed
- ✔ Authentication working
- ✔ Ticket system functional
- ✔ GitHub connected
- ✔ Render deployment ready

---

## 👨‍💻 Author

**Hemanth Sai**

---

## ⭐ Note

This project is suitable for:
- Resume projects
- College final year project
- Backend interviews
- FastAPI practice