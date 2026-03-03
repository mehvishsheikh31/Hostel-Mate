#🏨 Hostel Mate – Grievance Management System

A full-stack web application built with Django to digitize and streamline hostel complaint management.
The system enables structured complaint tracking, role-based access control, and real-time administrative insights.

🔗 **Live Application:**
[https://mehvishsheikh31.pythonanywhere.com/](https://mehvishsheikh31.pythonanywhere.com/)

---

## 🚀 Core Features

### 👨‍🎓 Student Portal

* Secure user registration and login
* Complaint submission with category and priority
* Complaint history tracking
* Image upload for issue proof
* Real-time status updates (Pending / In Progress / Resolved)

### 👮 Admin Dashboard

* View and manage all complaints
* Update complaint status and add remarks
* Filter by category, priority, and status
* Analytics dashboard with complaint trends
* Resolution tracking metrics

---

## 🧠 System Architecture

Client (Browser)
↓
Django Templates + Bootstrap UI
↓
Django Backend (MVT Architecture)
↓
Django ORM
↓
SQLite Database (Production-ready for MySQL/PostgreSQL)

---

## 🗄 Database Design

* One-to-many relationship between **User** and **Complaint**
* Controlled choices for:

  * Status (Pending / In Progress / Resolved)
  * Category (Water, Electricity, Cleaning, etc.)
  * Priority (Low / Medium / High)
* Timestamp tracking (`created_at`, `updated_at`)
* Optional image upload for complaint validation
* Admin remarks field for lifecycle tracking

The relational schema is implemented using Django ORM.

---

## 📊 Technology Stack

| Layer          | Technology                                        |
| -------------- | ------------------------------------------------- |
| Backend        | Django 5 (Python)                                 |
| Frontend       | HTML5, CSS3, Bootstrap 5                          |
| Database       | SQLite (Development), MySQL/PostgreSQL Compatible |
| Authentication | Django Built-in Auth System                       |
| Visualization  | Chart.js                                          |
| Deployment     | PythonAnywhere                                    |

---

## 🔐 Security Features

* Django authentication system
* Password hashing
* CSRF protection
* ORM-based protection against SQL injection
* Role-based access control

---

## ⚙️ Run Locally

Clone the repository:

```bash
git clone https://github.com/mehvishsheikh31/Hostel-Mate.git
cd Hostel-Mate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

## 📌 Project Highlights

* Structured relational database design
* Role-based complaint workflow management
* Real-time analytics dashboard
* Production-style full-stack architecture
* Deployed live on PythonAnywhere

