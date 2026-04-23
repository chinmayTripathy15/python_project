# 🔧 User Management REST API

A Python-based **REST API project** built using Flask that performs CRUD operations on user data.

---

## 📌 HTTP Methods Used (Core Concept)

### 🔹 GET → Read Data
- Used to **fetch data**
- Does NOT change anything

Example:
GET /users  
👉 Returns all users

---

### 🔹 POST → Create Data
- Used to **add new data**
- Sends data in JSON format

Example:
POST /users  

Body:
{
  "name": "Chinmay",
  "email": "chinmay@gmail.com"
}

👉 Adds a new user

---

### 🔹 PUT → Update Data
- Used to **modify existing data**
- Requires user ID

Example:
PUT /users/1  

Body:
{
  "name": "Updated Name",
  "email": "updated@gmail.com"
}

👉 Updates user with ID = 1

---

### 🔹 DELETE → Remove Data
- Used to **delete data**
- Requires user ID

Example:
DELETE /users/1  

👉 Deletes user with ID = 1

---

## 📊 Summary Table

| Method | Purpose       | Endpoint        |
|--------|--------------|----------------|
| GET    | Read data     | /users         |
| POST   | Create data   | /users         |
| PUT    | Update data   | /users/{id}    |
| DELETE | Delete data   | /users/{id}    |

---

## 🎯 Simple Flow

1. POST → Add user  
2. GET → See users  
3. PUT → Update user  
4. DELETE → Remove user  

---

## 🧠 Key Concept

REST API works using:
- HTTP Methods (GET, POST, PUT, DELETE)
- JSON data format
- Client ↔ Server communication

---

## 📌 Note

These methods form the base of almost all backend systems like:
- Login systems  
- E-commerce apps  
- Social media apps  