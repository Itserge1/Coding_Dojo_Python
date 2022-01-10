from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.userinfo import Userinfo

@app.route("/")
def create():
    return render_template("create.html")

@app.route("/prossec", methods=["POST"])
def prossec():
    data = {
        "first_name": request.form["fist_name"],
        "last_name": request.form["last_name"],
        "email":request.form["email"],
    }
    Userinfo.insert_userinfo(data)
    # session["fist_name"] = request.form["fist_name"]
    # session["last_name"] = request.form["last_name"]
    # session["email"] = request.form["email"]
    return redirect("/read")

@app.route("/read")
def read():
    Users = Userinfo.readalluser()
    return render_template("read.html", users = Users)

@app.route("/showinfo/<int:id>")
def showinfo(id):
    data = {
        "id":id
    }
    Users = Userinfo.readuser(data)
    return render_template("showinfo.html", users = Users)

@app.route("/edit/<int:id>")
def edit(id):
    data = {
        "id":id
    }
    Users = Userinfo.edituser(data)
    return render_template("edit.html", users = Users)

@app.route("/edituser/<int:id>", methods = ["POST"])
def editusers(id):
    data = {
        "first_name": request.form["fist_name"],
        "last_name": request.form["last_name"],
        "email":request.form["email"],
        "id":id
    }
    Userinfo.real_edituser(data)
    return redirect("/read")

@app.route("/delete/<int:id>")
def delete(id):
    data = {
        "id":id
    }
    Userinfo.deleteuser(data)
    return redirect("/")