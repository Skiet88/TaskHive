# Task Management Web App

## Overview

This is a Flask-based web application for managing personal tasks. Users can register, log in, create, edit, and delete tasks. The app features user authentication, form validation, and a user-friendly dashboard.

### App Structure

- `controller/`: Contains route controllers (e.g., `TaskController.py`) for handling web requests.
- `forms.py`: Defines all WTForms-based forms for user registration, login, profile editing, password change, and task management.
- `service/`: Contains business logic and database interaction (e.g., `TaskService.py`).
- `helpers.py`: Utility functions and decorators (e.g., login required, apology rendering).
- `templates/`: HTML templates for rendering pages.
- `static/`: Static files (CSS, JS, images).

## Setup Instructions

1. **Clone the repository:** 
   ```bash
   git clone https://github.com/Skiet88/TaskHive.git
2. **Create and activate a virtual environment:**
    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies:**
    ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Click on the link provided in the terminal to access the app in your web browser.
6. **Create an account or log in** to start managing using  default credentials:
   - Username: `user@account.com`
   - Password: `password123`

## Libraries Used

- **Flask**: Web framework
- **Flask-WTF**: WTForms integration for Flask (form handling and CSRF protection)
- **WTForms**: Form validation and rendering
- **Flask-Login**: User session management
- **email_validator**: Email validation for forms
- **requests**: HTTP requests (used in helpers)
- **Other**: Standard Python libraries (`datetime`, etc.)

---
