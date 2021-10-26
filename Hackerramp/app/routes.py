from flask import render_template, request
from werkzeug.utils import redirect
from app import app

bill = 0

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/billing", methods=["POST"])
def handleBilling():
    bill = request.form.values()
    return redirect("/dashboard")
