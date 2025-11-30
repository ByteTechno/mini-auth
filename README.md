# MiniAuth
A minimum user authentication system based on Flask + SQLite, supporting registration, login, and logout, and using encrypted passwords and sessions to manage user status.

## ✅ Function list
- User registration (Automatically encrypted password)
- User login (Verify encrypted password)
- User logout (Clear login status)
- Login status retention (via Flask Session)
- The page is beautified using Bootstrap
- Complete template structure: Jinja2 template inheritance (base/login/register/home)

## 📁 Directory structure
MiniAuth/
├── app.py                          # Main program entry, including all backend logic
├── users.db                        # SQLite database file (Automatically generated for the first run)
└── templates/                      # Page template directory
    ├── base.html                   # Master Template (Inherited by all pages)
    ├── login.html                  # login page
    ├── register.html               # Registration page
    └── home.html                   # The homepage after logging in

## 🚀 Startup mode
Make sure you have installed Flask:
pip install flask
Then run the project:
python app.py
Open a browser and visit:
http://127.0.0.1:5000/
It will redirect to the login page for the first time.

## 🔐 Default Settings Description
* User data is stored in the "users.db" database
* password using "werkzeug. Security. Generate_password_hash" encrypted storage
* The login status is managed through 'Flask session' (with 'app.secret_key' set)

## 💡 Teaching Objectives
This project is suitable as:
* The starting point for Web beginners to learn the Flask user system
* The foundation of the authentication module for subsequent projects (such as blogs, back-end systems, and code platforms)
* Practice building a complete process of "login → home page → logout" by yourself

## 📦 Future Expandable Functions （TODO）
* "Remember Me" feature (using cookies)
* User avatar/email field
* Flask Blueprint modular structure
* Database migration support (such as Flask-Migrate)
