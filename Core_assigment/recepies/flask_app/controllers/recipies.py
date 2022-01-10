from flask.helpers import flash
from flask_app import app
from flask import render_template, redirect, request,session
from flask_app.models.recipie import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# *********************************************
#              NEW RECEPIE ROUTE
# *********************************************

@app.route("/recepies/new")
def recepies():
    return render_template("recepies.html")

# *********************************************
#            PROCESS RECEPIE ROUTE
# *********************************************

@app.route("/processrecepies", methods = ["POST"])
def process_recepies():
    if Recipe.validate_recipie(request.form):
        data = {
            "name": request.form["name"],
            "description": request.form["description"],
            "instruction": request.form["instruction"],
            "date": request.form["date"],
            "time": request.form["time"],
            "user_id": session["user_id"]
        }
        Recipe.insert_recipies(data)
        return redirect("/dashboard")
    else:
        return redirect("/recepies/new")

# *********************************************
#               EDIT ROUTE
# *********************************************

@app.route("/recepies/<int:id>")
def info_recepies(id):
    data = {
        "user_id" : id
    }
    Recipies = Recipe.display_user_recipies(data)
    return render_template("inforecepies.html", recepie = Recipies)


# *********************************************
#              GET RECIPIE ROUTE
# *********************************************

@app.route("/recepies/edit/<int:id>")
def get_recepies(id):
    data = {
        "user_id" : id
    }
    db_recipies = Recipe.get_recipies(data)
    return render_template("update.html", recepie = db_recipies[0])

@app.route("/edituser/<int:id>", methods = {"POST"})
def edit_recepies(id):
    if Recipe.validate_recipie(request.form):
        data = {
            "name": request.form["name"],
            "description": request.form["description"],
            "instruction": request.form["instruction"],
            "date": request.form["date"],
            "time": request.form["time"],
            "user_id" : id
        }
        db_recipies = Recipe.update_recipies(data)
        return redirect("/dashboard")
    else:
        return redirect("/recepies/edit/<int:id>")

