from flask import Flask, render_template, request
from strength_service import PasswordChecker

app = Flask(__name__)

def save_to_db():
    pass

def get_history():
    pass

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/check", methods=["POST"])  
def check():
    password = request.form["password"]
    checker = PasswordChecker(password)
    rating = checker.get_password_rating() 
    return render_template("result.html", password=password, rating=rating) 

@app.route("/history")
def history():
    pass
    history = get_history()
return render_template(history.html, history=history)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)