# Project-Employee_Management

# Employee Management System

## 📌 Project Overview

The Employee Management System is a web-based application developed using the Django framework that helps organizations efficiently manage employee records, attendance, salaries, and leave requests. The system provides an easy-to-use interface for administrators to manage employee-related information and track organizational activities.

This project demonstrates the implementation of CRUD operations, database relationships, form handling, and employee workflow management using Django.

---

## 🚀 Features

### Admin Features

- Add new employees
- View employee details
- Update employee information
- Delete employee records
- Manage attendance records
- Manage salary information
- View leave requests
- Approve or reject leave requests

### Employee Features

- View personal profile
- Check attendance records
- View salary details
- Apply for leave
- Track leave request status

---

## 🛠️ Technology Stack

### Backend
- Python
- Django

### Frontend
- HTML5
- CSS3

### Database
- SQLite3

### Other Technologies
- Django ORM
- Django Forms
- Session Management

---

## 📂 Project Structure

```text
Employee_Management_System/
│
├── Employee/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── Employee_Management_System/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 🗄️ Database Models

### Employee_Details

Stores employee information.

| Field | Description |
|---------|-------------|
| Name | Employee Name |
| Email | Employee Email |
| Department | Department Name |
| Salary | Employee Salary |
| Age | Employee Age |
| Username | Login Username |
| Password | Login Password |

---

### Attendance

Stores employee attendance records.

| Field | Description |
|---------|-------------|
| Employee | Foreign Key to Employee |
| Date | Attendance Date |
| Status | Present / Absent |

Example:

```python
class Attendance(models.Model):

    employee = models.ForeignKey(
        Employee_Details,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    status = models.CharField(
        max_length=20
    )
```

---

### Leave_Request

Stores employee leave requests.

| Field | Description |
|---------|-------------|
| Employee | Foreign Key to Employee |
| Reason | Leave Reason |
| Status | Pending / Approved / Rejected |

Example:

```python
class Leave_Request(models.Model):

    employee = models.ForeignKey(
        Employee_Details,
        on_delete=models.CASCADE
    )

    reason = models.TextField()

    status = models.CharField(
        max_length=20
    )
```

---

### Salary

Stores employee salary details.

| Field | Description |
|---------|-------------|
| Employee | Foreign Key to Employee |
| Amount | Salary Amount |
| Month | Salary Month |

---

## 🔗 Relationships

```text
Employee_Details
       │
       ├── Attendance
       │
       ├── Salary
       │
       └── Leave_Request
```

One employee can have:

- Multiple attendance records
- Multiple salary records
- Multiple leave requests

This relationship is implemented using Django Foreign Keys.

---

## ⚙️ Installation Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/employee-management-system.git
```

### Step 2: Navigate to Project Directory

```bash
cd employee-management-system
```

### Step 3: Create Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Step 5: Install Dependencies

```bash
pip install django
```

### Step 6: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Create Superuser

```bash
python manage.py createsuperuser
```

### Step 8: Run Server

```bash
python manage.py runserver
```

### Step 9: Open Browser

```text
http://127.0.0.1:8000/
```

---

## 💻 Key Django Concepts Used

### Models

Used for database table creation.

```python
class Employee_Details(models.Model):
    name = models.CharField(max_length=100)
```

### Forms

Used for accepting user input.

```python
class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee_Details
        fields = "__all__"
```

### Views

Used to handle requests and responses.

```python
def Employee_list(request):
    employee = Employee_Details.objects.all()
    return render(
        request,
        'employee_list.html',
        {'employee': employee}
    )
```

### Templates

Used to display data in HTML pages.

```html
{% for emp in employee %}
    <tr>
        <td>{{ emp.name }}</td>
    </tr>
{% endfor %}
```

---

## 📸 Modules Implemented

### Employee Module

- Add Employee
- Update Employee
- Delete Employee
- Employee Profile

### Attendance Module

- Add Attendance
- View Attendance

### Salary Module

- Add Salary
- View Salary Records

### Leave Management Module

- Apply Leave
- Approve Leave
- Reject Leave
- View Leave History

---

## 🎯 Learning Outcomes

Through this project, the following concepts were learned:

- Django Framework
- Django ORM
- CRUD Operations
- Model Relationships
- Foreign Keys
- Form Handling
- URL Routing
- Template Rendering
- Database Management
- Employee Workflow Automation
- Session Handling

---

## 🔮 Future Enhancements

- Django Authentication System
- Password Hashing
- Role-Based Access Control
- Employee Dashboard
- Attendance Reports
- Payroll Automation
- Search Functionality
- Export Reports to Excel/PDF
- Email Notifications
- REST API Development

---

## 📈 Project Highlights

- Developed a complete Employee Management System using Django.
- Implemented CRUD functionality for employee records.
- Managed attendance, salary, and leave information.
- Used Django ORM for database operations.
- Designed responsive user interfaces using HTML and CSS.
- Established one-to-many relationships using Foreign Keys.
- Improved understanding of real-world business workflow applications.

---

## 👩‍💻 Author

### Subaranjani S

Python Full Stack Developer

---

## 📄 Resume Description

**Employee Management System | Python, Django, SQLite**

Developed a web-based Employee Management System using Django to streamline employee record management, attendance tracking, salary processing, and leave request handling. Implemented CRUD operations, database relationships using Django ORM, form validation, and session management. Built responsive user interfaces with HTML and CSS while managing employee workflows through an integrated system.
