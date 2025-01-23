# Employee Management System

## Description
A Django-based Employee Management System that allows adding, updating, and deleting employee records, including their salary, designation, and other information.

## Features
- User authentication (register, login, logout).
- Add, update, and delete employee information.
- Form validation for fields like phone number.
- Data storage in SQLite database.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nozibuddowla/employee_management

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Set up the database:
    ```bash
    python manage.py migrate

4. Run the development server:
    ```bash
    python manage.py runserver

5. Access the application at http://localhost:8000/

## Usage
- Register an account.
- Add employee details like name, phone number, email, salary, and designation.
- Update and delete employee information.