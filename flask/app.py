import sqlite3
from strength_service import PasswordChecker
from flask import Flask, render_template, request

app = Flask(__name__)

def save_to_db(password, rating):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (password, rating) VALUES(?, ?)", (password, rating))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password, rating FROM history")
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/check", methods=["POST"])  
def check():
    password = request.form["password"]
    checker = PasswordChecker(password)
    rating = checker.get_password_rating()
    save_to_db(password, rating) 
    return render_template("result.html", password=password, rating=rating) 

@app.route("/history")
def history():
    history = get_history()
    return render_template("history.html", history=history)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)