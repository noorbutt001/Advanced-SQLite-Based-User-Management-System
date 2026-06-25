# Advanced SQLite-Based User Management System

## Overview

The Advanced SQLite-Based User Management System is a Python application that provides secure user account management using SQLite as the database backend. The system supports user registration, authentication, profile management, and database operations through a simple and user-friendly interface.

## Features

* User Registration
* User Login and Authentication
* SQLite Database Integration
* Password Validation
* User Data Storage and Retrieval
* Update User Information
* Delete User Accounts
* Search Users
* View All Registered Users
* Error Handling and Input Validation
* Modular Project Structure

## Technologies Used

* Python 3.x
* SQLite3
* Object-Oriented Programming (OOP)
* File Handling
* Command Line Interface (CLI)

## Project Structure

```text
Advanced SQLite-Based User Management System/
│
├── main.py
├── database.py
├── user_manager.py
├── models.py
├── utils.py
├── requirements.txt
├── README.md
└── database.db
```

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Advanced SQLite-Based User Management System
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

Execute the main file:

```bash
python main.py
```

## Database

The application uses SQLite for persistent data storage.

Database file:

```text
database.db
```

Sample user table structure:

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
```

## Functionalities

### Register User

Allows creation of a new user account.

### Login User

Authenticates users using stored credentials.

### View Users

Displays all registered users from the database.

### Update User

Updates existing user information.

### Delete User

Removes a user from the database.

### Search User

Finds users by username or email.

## Security Considerations

* Validate user inputs before storing.
* Use password hashing in production environments.
* Prevent SQL injection using parameterized queries.
* Restrict database access permissions.

## Future Enhancements

* Password Hashing (bcrypt)
* GUI using Tkinter
* Web Interface using Flask
* Role-Based Access Control
* Export Data to CSV/Excel
* Email Verification
* Audit Logging

## Author

Noor Semab 

## License

This project is intended for educational and learning purposes.
