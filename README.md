# 🏏 Cricket Ranking System

## 📌 Overview

The **Cricket Ranking System** is a web-based application built using **Django** and **Django REST Framework** that allows users to manage and view cricket player rankings across different formats such as **ODI, T20, and Test**.

This project was developed as part of an **Internship I did in CDAC in May 2025**.

---

## 🚀 Features

* ➕ Add new players
* ✏️ Update player details
* ❌ Delete players
* 📋 View player list
* 📊 View rankings:

  * ODI Rankings
  * T20 Rankings
  * Test Rankings
* 🔍 Organized and structured backend using Django

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** SQLite
* **Frontend:** HTML, CSS (basic templates)

---

## 📁 Project Structure

```
project1/
│
├── app1/              # Main application (models, views, serializers)
├── html_file/         # HTML templates
├── project1/          # Django project settings
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Madhav1303/Cricket-Ranking.git
cd Cricket-Ranking/project1
```

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
```

### 3️⃣ Activate virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

---

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Run migrations

```bash
python manage.py migrate
```

---

### 6️⃣ Run the server

```bash
python manage.py runserver
```

---

### 7️⃣ Open in browser

```
http://127.0.0.1:8000/
```

---

## 📌 API Endpoints (Sample)

* `/players/` → View all players
* `/add/` → Add player
* `/update/` → Update player
* `/delete/` → Delete player
* `/odiranking/` → ODI rankings
* `/t20rankings/` → T20 rankings
* `/testrankings/` → Test rankings

---

## 📊 Future Improvements

* 🌐 Deploy project (Render / Vercel / Railway)
* 🎨 Improve UI with React or modern frontend
* 🔐 Add authentication (Login/Register)
* 📈 Add advanced filtering and search

---

## 🤝 Contribution

Contributions are welcome! Feel free to fork this repo and improve it.

---

## 📄 License

This project is for educational purposes.

---

## 👨‍💻 Author

**Madhav Kishore K S**<br>
B.Tech CSE (Data Science)<br>
VIT Vellore

---
