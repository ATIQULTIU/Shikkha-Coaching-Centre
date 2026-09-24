<div align="center">

# 🎓 Shikkha Coaching Centre Management System

**A Flask-based web application for managing students, teachers, batches, attendance, fees, and notices from one admin dashboard.**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

</div>

---

## 📑 Table of Contents

- [Project Description](#-project-description)
- [Quick Start](#-quick-start)
- [Default Admin Credentials](#-default-admin-credentials)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [Project Architecture](#-project-architecture)
- [System Requirements](#-system-requirements)
- [Installation](#-installation)
- [Virtual Environment Setup](#-virtual-environment-setup)
- [Dependency Installation](#-dependency-installation)
- [How to Run](#-how-to-run-the-project)
- [Dashboard Overview](#-dashboard-overview)
- [Admin Workflow](#-admin-workflow)
- [Modules in Detail](#-modules-in-detail)
- [Database Information](#-database-information)
- [Security Information](#-security-information)
- [UI and Responsive Design](#-ui-and-responsive-design)
- [Testing Instructions](#-testing-instructions)
- [Troubleshooting](#-troubleshooting)
- [Future Improvements](#-future-improvements)
- [Production Deployment Suggestions](#-production-deployment-suggestions)
- [Environment Variables](#-environment-variables)
- [Git Commands for Pushing Updates](#-git-commands-for-pushing-updates)
- [Developer Information](#-developer-information)
- [License](#-license)
- [Support](#-support)

---

## 📖 Project Description

**Shikkha Coaching Centre Management System** is a web-based administration tool built with **Python** and **Flask** for coaching centres. It replaces paper registers and scattered spreadsheets with a single, organized dashboard.

An administrator can log in and manage:

- Student records and admission approval
- Teacher records and their subjects
- Batches with assigned teachers and schedules
- Daily attendance for each batch
- Fee payments and payment history
- Notices and announcements

The project uses **Flask-SQLAlchemy** with a lightweight **SQLite** database, so it runs locally with no extra database server. The interface uses **Jinja2** templates with custom **HTML5**, **CSS3**, and **JavaScript**, and it is responsive across screen sizes.

---

## ⚡ Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/ATIQULTIU/Shikkha-Coaching-Centre.git
cd Shikkha-Coaching-Centre

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python app.py
```

Then open **http://127.0.0.1:5000** in your browser and log in with the [default admin credentials](#-default-admin-credentials).

> 💡 It is recommended to use a [virtual environment](#-virtual-environment-setup) before installing dependencies.

---

## 🔐 Default Admin Credentials

| Field    | Value       |
| -------- | ----------- |
| Username | `admin`     |
| Password | `Admin@123` |

> ⚠️ **Important:** Change the default password immediately after your first login from the **Settings** page. Never deploy with default credentials.

---

## ✨ Key Features

| # | Module | Capabilities |
|---|--------|--------------|
| 1 | 🔑 **Authentication** | Admin login and authentication |
| 2 | 📊 **Admin Dashboard** | Central overview of the coaching centre |
| 3 | 🧑‍🎓 **Student Management** | Add, edit, delete, approve, and reject students; manage student status |
| 4 | 👨‍🏫 **Teacher Management** | Add, edit, and delete teachers; subject management |
| 5 | 📚 **Batch Management** | Add, edit, and delete batches; assign teachers; manage schedules |
| 6 | 🗓️ **Attendance Management** | Select batch and date, mark Present/Absent, update attendance |
| 7 | 💰 **Fee Management** | Record payments, track payment status, view payment history |
| 8 | 📢 **Notice Management** | Add, edit, and delete notices and announcements |
| 9 | ⚙️ **Admin Settings** | Admin profile, admin email, change password |
| 10 | 📱 **Responsive UI** | Responsive admin dashboard |

---

## 🛠️ Technology Stack

| Layer | Technology |
|-------|------------|
| **Language** | Python |
| **Backend Framework** | Flask |
| **ORM** | Flask-SQLAlchemy |
| **Database** | SQLite |
| **Templating** | Jinja2 |
| **WSGI / Utilities** | Werkzeug |
| **Frontend** | HTML5, CSS3, JavaScript |

---

## 🏗️ Project Architecture

### Folder Structure

```text
Shikkha-Coaching-Centre/
├── app.py                  # Flask app, models, and routes
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Files ignored by Git
├── static/
│   ├── css/
│   │   └── style.css       # Application styles
│   └── js/
│       └── app.js          # Client-side scripts
└── templates/
    ├── base.html           # Base layout (inherited by all pages)
    ├── login.html          # Admin login page
    ├── dashboard.html      # Admin dashboard
    ├── students.html       # Student list
    ├── student_form.html   # Add / edit student form
    ├── teachers.html       # Teacher list
    ├── teacher_form.html   # Add / edit teacher form
    ├── batches.html        # Batch list
    ├── batch_form.html     # Add / edit batch form
    ├── attendance.html     # Attendance marking page
    ├── fees.html           # Fee records and payments
    ├── notices.html        # Notice list
    ├── notice_form.html    # Add / edit notice form
    └── settings.html       # Admin settings
```

### Architecture Overview

The project follows a simple server-rendered MVC-style pattern:

| Component | Location | Responsibility |
|-----------|----------|----------------|
| **Model** | `app.py` (Flask-SQLAlchemy models) | Defines database tables and relationships |
| **View / Controller** | `app.py` (Flask routes) | Handles requests, business logic, and responses |
| **Template** | `templates/` (Jinja2) | Renders HTML pages |
| **Static Assets** | `static/` | CSS and JavaScript for the UI |

---

## 💻 System Requirements

| Requirement | Details |
|-------------|---------|
| **Python** | 3.8 or higher recommended |
| **pip** | Python package manager |
| **Git** | For cloning the repository |
| **Browser** | Any modern browser (Chrome, Firefox, Edge, Safari) |
| **OS** | Windows, Linux, or macOS |

Check your Python version:

```bash
python --version
```

---

## 📥 Installation

**1. Clone the repository**

```bash
git clone https://github.com/ATIQULTIU/Shikkha-Coaching-Centre.git
```

**2. Move into the project directory**

```bash
cd Shikkha-Coaching-Centre
```

**3. Create a virtual environment and install dependencies** (see the next two sections).

---

## 🧪 Virtual Environment Setup

A virtual environment keeps the project's dependencies isolated from your system Python.

### 🪟 Windows

```bash
# Create the virtual environment
python -m venv venv

# Activate (Command Prompt)
venv\Scripts\activate

# Activate (PowerShell)
venv\Scripts\Activate.ps1
```

> If PowerShell blocks activation, run once: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

### 🐧 Linux / 🍎 macOS

```bash
# Create the virtual environment
python3 -m venv venv

# Activate
source venv/bin/activate
```

### Deactivate (all platforms)

```bash
deactivate
```

---

## 📦 Dependency Installation

With the virtual environment activated:

```bash
pip install -r requirements.txt
```

To upgrade pip first (optional):

```bash
python -m pip install --upgrade pip
```

---

## ▶️ How to Run the Project

```bash
python app.py
```

Then open your browser at:

```text
http://127.0.0.1:5000
```

Use `Ctrl + C` in the terminal to stop the server.

---

## 📊 Dashboard Overview

After logging in, the admin lands on the **Dashboard**, the central control panel of the system. From here, the admin can navigate to every module:

| Section | Purpose |
|---------|---------|
| Dashboard | Overview of the coaching centre |
| Students | Manage admissions and student records |
| Teachers | Manage teacher records and subjects |
| Batches | Manage batches, teachers, and schedules |
| Attendance | Mark and update daily attendance |
| Fees | Record payments and view history |
| Notices | Publish and manage announcements |
| Settings | Update profile, email, and password |

---

## 🔄 Admin Workflow

```text
                        ┌──────────────────┐
                        │   Admin Login    │
                        └────────┬─────────┘
                                 │
                        ┌────────▼─────────┐
                        │    Dashboard     │
                        └────────┬─────────┘
        ┌───────────┬────────────┼────────────┬────────────┬───────────┐
        │           │            │            │            │           │
  ┌─────▼─────┐┌────▼────┐ ┌─────▼─────┐┌─────▼─────┐┌─────▼────┐┌─────▼─────┐
  │ Teachers  ││ Batches │ │ Students  ││Attendance ││   Fees   ││  Notices  │
  └─────┬─────┘└────┬────┘ └─────┬─────┘└─────┬─────┘└─────┬────┘└─────┬─────┘
        │           │            │            │            │           │
   Add / Edit   Add / Edit   Add / Edit   Select Batch   Record     Add / Edit
   / Delete     / Delete     / Delete     Select Date    Payment    / Delete
   Subjects     Assign       Approve /    Mark Present   Check      Announce
                Teacher      Reject       / Absent       Status
                Schedule     Set Status   Update         View
                                                         History
                                 │
                        ┌────────▼─────────┐
                        │ Settings/Logout  │
                        └──────────────────┘
```

**Recommended setup order for a new coaching centre:**

```text
1. Add Teachers  →  2. Create Batches  →  3. Add / Approve Students
      →  4. Take Attendance  →  5. Record Fees  →  6. Post Notices
```

---

## 🧩 Modules in Detail

### 🧑‍🎓 Student Management

Manages the complete student record lifecycle.

**Workflow:**

```text
Add Student → Pending Review → Approve ✅ / Reject ❌ → Manage Status
```

| Action | Description |
|--------|-------------|
| **Add** | Register a new student using the student form |
| **Edit** | Update an existing student's information |
| **Delete** | Remove a student record |
| **Approve** | Accept a student's admission |
| **Reject** | Decline a student's admission |
| **Status Management** | Track and update each student's current status |

### 👨‍🏫 Teacher Management

| Action | Description |
|--------|-------------|
| **Add** | Add a new teacher record |
| **Edit** | Update teacher details |
| **Delete** | Remove a teacher record |
| **Subject Management** | Manage the subject(s) associated with each teacher |

### 📚 Batch Management

| Action | Description |
|--------|-------------|
| **Add** | Create a new batch |
| **Edit** | Update batch details |
| **Delete** | Remove a batch |
| **Assign Teacher** | Link a teacher to a batch |
| **Schedule Management** | Set and update batch class schedules |

### 🗓️ Attendance Management

**Workflow:**

```text
Select Batch → Select Date → Mark Present / Absent → Save → (Update later if needed)
```

- Choose the batch and the date
- Mark each student as **Present** or **Absent**
- Update previously saved attendance when corrections are needed

### 💰 Fee Management

| Feature | Description |
|---------|-------------|
| **Record Payments** | Enter payments received from students |
| **Payment Status** | View whether a fee is paid or not |
| **Payment History** | Review previous payment records |

### 📢 Notice Management

| Action | Description |
|--------|-------------|
| **Add** | Publish a new notice |
| **Edit** | Modify an existing notice |
| **Delete** | Remove a notice |
| **Announcements** | Share important announcements for the coaching centre |

### ⚙️ Admin Settings

| Setting | Description |
|---------|-------------|
| **Admin Profile** | View and update admin profile information |
| **Admin Email** | Update the admin email address |
| **Change Password** | Replace the default password with a secure one |

---

## 🗄️ Database Information

The project uses **SQLite** through **Flask-SQLAlchemy**. No separate database server is required.

### Database Models

| Model | Purpose |
|-------|---------|
| `Admin` | Stores administrator account information |
| `Teacher` | Stores teacher records and their subjects |
| `Batch` | Stores batch details, schedules, and the assigned teacher |
| `Student` | Stores student records and admission status |
| `Attendance` | Stores attendance records per student, batch, and date |
| `Fee` | Stores payment records and payment status |
| `Notice` | Stores notices and announcements |

### Model Relationships (Conceptual)

```text
Teacher ──< Batch ──< Student
              │          │
              │          ├──< Attendance
              │          └──< Fee
              │
Admin (manages the whole system)      Notice (published by admin)
```

### Database File

The SQLite database file is created automatically when the application runs for the first time. Its exact location depends on how the application is configured in `app.py`, and it is usually inside the project directory or an `instance/` folder.

> 💡 Add the database file to `.gitignore` so that real student and fee data is never pushed to GitHub.

---

## 🔒 Security Information

| Topic | Notes |
|-------|-------|
| **Default credentials** | The default `admin / Admin@123` is for first-time setup only. Change it immediately. |
| **Password management** | Use the **Settings** page to change the admin password. |
| **Werkzeug** | Included in the stack; Werkzeug provides security utilities commonly used for password hashing. |
| **Secret key** | Use a long, random secret key in any real deployment (see [Environment Variables](#-environment-variables)). |
| **Debug mode** | Turn debug mode **off** in production. |
| **Sensitive data** | Do not commit the database file or any secrets to GitHub. |
| **HTTPS** | Serve the application over HTTPS in production. |

> ⚠️ This project is intended for learning and small-scale use. Review and harden the security configuration before any public deployment.

---

## 📱 UI and Responsive Design

- Clean admin dashboard layout built with **HTML5** and **CSS3**
- Shared layout through Jinja2 template inheritance (`base.html`)
- Responsive design for desktop, tablet, and mobile screens
- Client-side interactivity through `static/js/app.js`
- Centralized styling in `static/css/style.css`

---

## 🧪 Testing Instructions

Manual testing checklist:

| Module | What to Verify |
|--------|----------------|
| **Login** | Correct credentials succeed; wrong credentials are rejected |
| **Students** | Add, edit, delete, approve, and reject work correctly |
| **Teachers** | Add, edit, delete work; subject is saved |
| **Batches** | Add, edit, delete work; teacher assignment and schedule are saved |
| **Attendance** | Select batch and date; mark and update Present/Absent |
| **Fees** | Payments are recorded; status and history display correctly |
| **Notices** | Add, edit, and delete notices |
| **Settings** | Profile, email, and password updates work; login works with the new password |
| **Responsive** | Resize the browser or use developer tools' device mode |

**Testing steps:**

```bash
# 1. Start the app
python app.py

# 2. Open http://127.0.0.1:5000 and go through the checklist above
```

> 💡 Automated tests (for example with `pytest`) are listed under [Future Improvements](#-future-improvements).

---

## 🩺 Troubleshooting

| Problem | Possible Solution |
|---------|-------------------|
| `python` is not recognized | Install Python and add it to PATH, or try `python3` |
| `pip` is not recognized | Use `python -m pip install -r requirements.txt` |
| `ModuleNotFoundError: No module named 'flask'` | Activate the virtual environment and run `pip install -r requirements.txt` |
| Port 5000 already in use | Stop the other process using port 5000, or change the port in `app.py` |
| PowerShell blocks venv activation | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| Cannot log in | Use `admin` / `Admin@123`, or `Admin@123` may have been changed in Settings |
| Database errors after model changes | Back up your data, delete the old SQLite file, and restart so tables are recreated |
| Page styles not updating | Hard refresh with `Ctrl + F5` to clear the browser cache |
| Changes not reflected | Restart the Flask server |

---

## 🚀 Future Improvements

> The following are **planned ideas only**. They are **not** part of the current version.

- [ ] Email notifications
- [ ] SMS notifications
- [ ] Two-factor authentication (2FA)
- [ ] Student and teacher login portals
- [ ] Reports and data export (PDF / Excel)
- [ ] Search, filtering, and pagination
- [ ] Automated tests with `pytest`
- [ ] Database migrations with Flask-Migrate
- [ ] Docker support
- [ ] Migration to PostgreSQL or MySQL for production
- [ ] Role-based access control

---

## 🌐 Production Deployment Suggestions

The built-in Flask server (`python app.py`) is for **development only**. For production:

| Area | Recommendation |
|------|----------------|
| **WSGI server** | Use **Gunicorn** (Linux/macOS) or **Waitress** (Windows) |
| **Reverse proxy** | Place **Nginx** in front of the app |
| **HTTPS** | Enable SSL/TLS (for example with Let's Encrypt) |
| **Debug mode** | Disable `debug=True` |
| **Secret key** | Load from an environment variable, never hard-code it |
| **Database** | Consider PostgreSQL or MySQL for larger deployments |
| **Backups** | Schedule regular database backups |
| **Default password** | Change the admin password before going live |
| **Hosting options** | VPS, PythonAnywhere, Render, Railway, or similar platforms |

Example with Gunicorn (Linux/macOS):

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

Example with Waitress (Windows):

```bash
pip install waitress
waitress-serve --port=8000 app:app
```

---

## 🔧 Environment Variables

> These variables are **recommended for production**. Depending on your `app.py`, you may need to read them in code using `os.environ.get(...)`.

| Variable | Purpose | Example |
|----------|---------|---------|
| `SECRET_KEY` | Secret key for securing sessions | `a-long-random-string` |
| `DATABASE_URL` | Database connection string | `sqlite:///shikkha.db` |
| `FLASK_DEBUG` | Enable or disable debug mode | `0` |

Example `.env` file (do not commit this file):

```env
SECRET_KEY=change-this-to-a-long-random-string
DATABASE_URL=sqlite:///shikkha.db
FLASK_DEBUG=0
```

Setting a variable in the terminal:

```bash
# Linux / macOS
export SECRET_KEY="your-secret-key"

# Windows (Command Prompt)
set SECRET_KEY=your-secret-key

# Windows (PowerShell)
$env:SECRET_KEY="your-secret-key"
```

---

## 🔀 Git Commands for Pushing Updates

**First-time setup:**

```bash
git init
git remote add origin https://github.com/ATIQULTIU/Shikkha-Coaching-Centre.git
git branch -M main
```

**Pushing updates:**

```bash
# Check what changed
git status

# Stage all changes
git add .

# Commit with a clear message
git commit -m "Describe your update here"

# Push to GitHub
git push origin main
```

**Pulling the latest changes:**

```bash
git pull origin main
```

**Recommended `.gitignore` entries:**

```gitignore
venv/
__pycache__/
*.pyc
*.db
*.sqlite3
instance/
.env
.vscode/
.idea/
```

---

## 👨‍💻 Developer Information

<div align="center">

**MD. Atiqul Islam (Atik)**

Software Engineering Student

[![Email](https://img.shields.io/badge/Email-atik.cmttiu1001%40gmail.com-D14836?logo=gmail&logoColor=white)](mailto:atik.cmttiu1001@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-ATIQULTIU-181717?logo=github&logoColor=white)](https://github.com/ATIQULTIU)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-00C4CC?logo=canva&logoColor=white)](https://md-atiqul-islam.my.canva.site/)

</div>

| Detail | Link |
|--------|------|
| 📧 Email | atik.cmttiu1001@gmail.com |
| 🐙 GitHub | https://github.com/ATIQULTIU |
| 🌐 Portfolio | https://md-atiqul-islam.my.canva.site/ |

---

## 📄 License

This project is licensed under the **MIT License**. Add a `LICENSE` file to the repository root to make the license official.

```text
MIT License

Copyright (c) MD. Atiqul Islam (Atik)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## ⭐ Support

If you find this project helpful:

- ⭐ **Star** this repository on GitHub
- 🍴 **Fork** it and build on it
- 🐛 **Report issues** or suggest improvements through GitHub Issues
- 📧 Contact the developer at **atik.cmttiu1001@gmail.com**

---

<div align="center">

**Developed with ❤️ by [MD. Atiqul Islam (Atik)](https://github.com/ATIQULTIU)**

🎓 *Shikkha Coaching Centre Management System*

</div>
