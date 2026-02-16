# 🏨 Hostel Mate - Smart Grievance Management System

![Project Status](https://img.shields.io/badge/Status-Live-success?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge) ![Django](https://img.shields.io/badge/Django-5.1-092E20?style=for-the-badge) ![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge)


> Transforming hostel maintenance from chaotic manual registers into a structured, transparent, and analytics-driven digital system.

**HostelMate is a production-oriented full-stack web application built to streamline complaint management, improve accountability, and empower administrators with actionable insights.**

---

## ⭐ Why HostelMate Exists

In most hostels:

- Complaints get lost in registers  
- No one tracks resolution time  
- Students lack transparency  
- Admin decisions are reactive, not data-driven  

**HostelMate eliminates these inefficiencies with automation, structured workflows, and real-time analytics.**

👉 Result: Faster resolutions, higher operational efficiency, and improved student experience.

---

## 🚀 Live Demo

🌐 **Live Application:**  
👉 *(https://mehvishsheikh31.pythonanywhere.com/)*

---

## 🧠 Architecture Overview

```

Browser (Client)
↓
Django Templates + Bootstrap UI
↓
Django Backend (MVT Architecture)
↓
Django ORM
↓
Database (SQLite → MySQL/PostgreSQL Ready)

```

### Design Principles

✔ Separation of concerns  
✔ Secure authentication  
✔ Scalable schema  
✔ Modular Django apps  
✔ Analytics-ready data model  

This is not just a CRUD app — it is structured like real operational software.

---

## 🔥 Core Capabilities

### 👨‍🎓 Student Portal
- Secure signup & login  
- Category-based complaint submission  
- Priority tagging (High / Medium / Low)  
- Real-time complaint tracking  
- Complete complaint history  
- Mobile-responsive interface  

---

### 👮 Admin Intelligence Dashboard
- Live operational metrics  
- Interactive charts powered by Chart.js  
- Complaint trend analysis  
- Resolution rate monitoring  
- Smart filtering & status control  
- Spam management  

👉 Moves administration from guesswork → **data-driven decision making**
--

## 🔥 Application Preview

| Admin Dashboard | Student Dashboard |
|----------------|------------------|
| ![](assets/admin-dashboard.png) | ![](assets/student-dashboard.png) |

| Complaint Submission | Login |
|---------------------|-------|
| ![](assets/complaint-form.png) | ![](assets/login.png) |


## 🛠️ Tech Stack

| Layer | Technology |
|--------|-------------|
| Backend | Django 5 |
| Frontend | HTML5, CSS3, Bootstrap 5 |
| Database | SQLite (Development), MySQL/PostgreSQL Ready |
| Visualization | Chart.js |
| Deployment | PythonAnywhere / Render |

---

## ⚙️ Local Setup

Clone the repository:

```bash
git clone https://github.com/mehvishsheikh31/Hostel-Mate.git
cd Hostel-Mate
````

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Start server:

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

## 🔐 Security Features

* CSRF protection enabled
* Django authentication system
* Password hashing
* ORM prevents SQL injection
* Role-restricted admin actions

Security is treated as a baseline — not an afterthought.

---

## 📊 What This Project Demonstrates

This project validates strong capability in:

✅ Full-stack development
✅ Backend architecture
✅ Database design
✅ Authentication systems
✅ Data visualization
✅ Admin workflow engineering
✅ Production-style thinking


---

## 🚧 Future Enhancements

Planned upgrades:

* 🔔 Email / SMS notifications
* 🤖 AI-based complaint categorization
* 📱 REST API for mobile integration
* 🐳 Docker containerization
* 📈 Advanced analytics dashboard


---

