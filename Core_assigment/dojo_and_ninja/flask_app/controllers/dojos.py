from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.dojo import Ninja
from flask_app.models.dojo import Dojo

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/adddojo", methods=["POST"])
def adddojos():
    data = {
        "name": request.form["name"]
    }
    Dojo.insert_dojo(data)
    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    dojos = Dojo.get_dojo()
    return render_template("dojos.html", dojo = dojos)

@app.route("/dojos/<int:id>")
def dojos_ninjas(id):
    data = {
        "id": id
    }
    ninjas = Ninja.get_ninja(data)
    return render_template("dojosninja.html", id=id, ninja = ninjas)

@app.route("/insertninjas", methods=["POST"])
def insert_ninjas():
    data = {
        "dojo_id": request.form["dojo_id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"]
    }
    Ninja.insert_ninja(data)
    return redirect("/ninjas")

@app.route("/ninjas")
def ninjas():
    dojos = Dojo.get_dojo()
    return render_template("ninjas.html", dojo = dojos)