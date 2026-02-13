# 🚀 FastAPI RBAC JWT Task Manager API

A secure Task Management REST API built using **FastAPI**, **SQLAlchemy**, and **JWT Authentication** with **Role-Based Access Control (RBAC)**.

This project demonstrates real-world backend engineering concepts like:

- Authentication (JWT)
- Authorization (RBAC)
- Dependency Injection
- Secure Password Hashing (bcrypt)
- Database ORM (SQLAlchemy)
- RESTful CRUD APIs
- Modular project architecture

---

## 📌 Features

- 🔐 JWT Authentication (Login/Register)
- 🛡 Role-Based Access Control (Admin/User)
- 👤 User Registration & Login
- 📝 Task CRUD Operations
- 🗄 SQLite Database with SQLAlchemy ORM
- 📦 Modular Folder Structure
- 🔒 Secure Password Hashing using Passlib

---
├── main.py
├── api/
│ ├──api.py
├── Auth/
│ ├── Auth_routes.py
│ ├── auth.py
│ ├── Dependencies.py
├── Database/
│ ├── database.py
├── Models/
│ ├── table.py
│ ├── Auth_schemas.py
│ ├── Task_schemas.py
## 🏗 Project Architecture


---

## ⚙️ Tech Stack

- FastAPI
- SQLAlchemy ORM
- SQLite
- Passlib (bcrypt)
- Python-Jose (JWT)
- Uvicorn

---

## 🗄 Database Models

### 👤 Users
- id
- username (unique)
- hashed_password
- role (default = "user")

### 📝 Task
- id
- task
- description
- owner_id (ForeignKey → Users.id)

---

## 🔐 Authentication Flow

1. User registers
2. User logs in
3. Server generates JWT token
4. Client sends token in `Authorization: Bearer <token>`
5. Protected routes verify token & role

---

## 🛡 RBAC (Role-Based Access Control)

| Role  | Permissions |
|--------|------------|
| user   | Create, Update own tasks |
| admin  | View tasks (admin-only route) |
| owner  | Delete own task |

---

## 🔌 API Endpoints

### 🔐 Auth Routes

POST `/Auth/register`  
POST `/Auth/login`

---

### 📝 Task Routes

POST `/CRUD/v1/Create`  
GET `/CRUD/v1/task/{id}`  
GET `/CRUD/v1/tasks` (admin only)  
PUT `/CRUD/v1/update/{id}`  
DELETE `/CRUD/v1/{id}`  

---

## ▶️ Run Locally
##First install all the requirements to run the model
run:pip install -r requirements.txt
Run Backend:uvicorn main:app --reload or python -m uvicorn main:app --reload
Then open another terminal and run cd Frontend
Run Frontend:streamlit run frontend.py or python -m streamlit run frontend.py


### 1️⃣ Clone the repo

```bash
git clone https://github.com/adarshbaghel612/Primetrade_AI.git
