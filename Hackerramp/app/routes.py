from flask import render_template, request
from werkzeug.utils import redirect
from app import app

bill = 0
progress = {
    "shirt": 4,
    "pant": 6,
    "shoes": 3,
    "cap": 5
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", progress=progress)

@app.route("/billing", methods=["POST"])
def handleBilling():
    bill = request.form.values()
    return redirect("/dashboard")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html")
