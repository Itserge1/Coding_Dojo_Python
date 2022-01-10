from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.userinfo import Userinfo

@app.route("/")
def create():
    return render_template("dashboard.html")

