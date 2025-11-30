from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "123xyz"

# ========================
# Create an SQLite Database (Automatically executed once)
# ========================
def init_db():
    if not os.path.exists("users.db"):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()
        print("✅ The database has been initialized")
init_db()

# ========================
# Login Function
# ========================
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        raw_password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user is None:
            return render_template("login.html", error="The user does not exist.")

        user_id, db_username, db_password_hash = user

        if check_password_hash(db_password_hash, raw_password):
            session["username"] = username
            return redirect("/")
        else:
            return render_template("login.html", error="Incorrect password")

    return render_template("login.html")

# ========================
# Registration Function
# ========================
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        raw_password = request.form["password"]
        password = generate_password_hash(raw_password)

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()

        if user:
            conn.close()
            return render_template("register.html", error="The username already exists")

        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return redirect("/login")

    return render_template("register.html")

# ========================
# Home Page
# ========================
@app.route("/")
def home():
    if "username" in session:
        return render_template("home.html", username=session["username"])
    else:
        return redirect("/login")

# ========================
# Log Out
# ========================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
