from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.users import User

# *****************************************************
#              SETTING UP HOME ROUTE
# *****************************************************

@app.route("/")
def hello():
    return render_template("home.html")

# *****************************************************
#           SETTING UP THE FORM PAGE ROUTER
# ***************************************************** 

@app.route("/dojos")
def dojos():
    return render_template("dojos.html")

# *****************************************************
#           SETTING UP INFO PROCESS ROUTER
# *****************************************************

@app.route("/prossec_info", methods =["POST"])
def prossec_info():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.insert_user(data)
    return redirect("/users")

# *****************************************************
#           SETTING UP USER INFO ROUTER
# *****************************************************

@app.route("/users")
def users_info():
    Users = User.dispay_alluser()
    return render_template("users.html", users = Users)

# *****************************************************
#           SETTING UP SHOW/ EDIT/ DELETE ROUTERS
# *****************************************************

@app.route("/show/<int:id>")
def show(id):
    data = {
        "id":id
    }
    Users = User.dispay_user(data)
    return render_template("show.html", users = Users)

@app.route("/edit/<int:id>")
def edit(id):
    data = {
        "id":id
    }
    Users = User.edit_user(data)
    return render_template("edit.html", users = Users)

@app.route("/edituser/<int:id>", methods = ["POST"])
def editusers(id):
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email":request.form["email"],
        "id":id
    }
    User.real_edituser(data)
    return redirect("/users")

@app.route("/delete/<int:id>")
def delete(id):
    data = {
        "id":id
    }
    Users = User.deleteuser(data)
    return redirect("/users")