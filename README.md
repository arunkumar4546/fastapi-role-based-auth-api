# 🔐 Role-Based Authentication & Authorization API using FastAPI

## 🚀 Project Overview

This project is a secure and scalable RESTful Authentication & Authorization system built using **FastAPI**.
It implements **JWT-based stateless authentication** along with **Role-Based Access Control (RBAC)** where different users have different permissions.

The system allows normal users to access only their own resources, while **Admin users can manage all users (view, update, delete).**

This project demonstrates real-world backend architecture practices including secure password hashing, token-based authentication, protected routes, role validation, and database integration.

---

## ✨ Key Features

### 🔑 Authentication

* User Registration with validation
* Secure Password Hashing using **Passlib (bcrypt)**
* Login with JWT Token generation
* Stateless Authentication using **JSON Web Tokens**
* Token verification middleware / dependency

### 👤 User Functionalities

* Access protected **Profile Route**
* View own user data
* Update own profile information
* Secure endpoint authorization

### 🛡️ Admin Functionalities (RBAC)

* View all registered users
* Update any user details
* Delete users from system
* Admin-only protected routes
* Role validation using JWT payload

### ⚙️ Backend Engineering Practices

* Modular FastAPI project structure (Routes / Models / Schemas / DB)
* SQLAlchemy ORM integration with MySQL
* Environment variable configuration using `.env`
* Global Exception Handling
* Request validation using **Pydantic**
* Dependency Injection usage
* Clean API documentation via Swagger UI

---

## 🛠️ Tech Stack

* **FastAPI**
* **Python**
* **MySQL**
* **SQLAlchemy ORM**
* **JWT (python-jose)**
* **Passlib (bcrypt)**
* **Pydantic**
* **Uvicorn**
* **Postman (API Testing)**

---

## 🔐 Authentication Flow

1. User registers with email & password
2. Password is hashed and stored securely
3. User logs in → JWT token is generated
4. Token must be passed in Authorization Header
5. Protected routes validate token
6. Role-based access decides permission (User / Admin)

---

## 📂 Project Structure

```
project/
│
├── routes/
├── models/
├── schemas/
├── database/
├── auth/
├── main.py
├── requirements.txt
└── .env
```

---

## ▶️ Run Locally

```bash
git clone <repo-url>
cd project-folder
pip install -r requirements.txt
uvicorn main:app --reload
```

Open Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

## 📌 Future Improvements

* Refresh Token Mechanism
* Email Verification System
* Password Reset Flow
* Role Hierarchy & Permission Table
* Docker Deployment
* Rate Limiting & API Security Enhancements

---

## 👨‍💻 Author

**Arun Kumar**

If you found this project useful, consider ⭐ starring the repository.
