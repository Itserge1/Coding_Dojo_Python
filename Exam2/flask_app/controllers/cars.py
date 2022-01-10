from flask.helpers import flash
from flask_app import app
from flask import render_template, redirect, request,session
from flask_app.models.car import Car
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# *********************************************
#              ADD CARS
# *********************************************

@app.route("/new")
def paintings():
    if "user_id" not in session:
        flash("Must be logged in")
        return redirect ("/")
    else:
        return render_template("newcar.html")

# *********************************************
#            INSERTS CARS
# *********************************************

@app.route("/insertcar", methods = ["POST"])
def insertpaintings():
    if Car.validate_car(request.form):
        data = {
                "price": request.form["price"],
                "model": request.form["model"],
                "make": request.form["make"],
                "year": request.form["year"],
                "description": request.form["description"],
                "user_id": session["user_id"]
            }
        Car.insert_car(data)
        return redirect("/dashboard")
    else:
        return redirect("/new")

# *********************************************
#           VIEW CAR
# *********************************************

@app.route("/show/<int:id>")
def edit_painting_info(id):
    if "user_id" not in session:
        flash("Must be logged in")
        return redirect ("/")
    else:
        data = {
        "id" : id
        }
    artist_painting = Car.get_cars_user(data)
    pikabo = Car.get_cars(data)
    return render_template("showcar.html", name = artist_painting, cars = pikabo)

# *********************************************
#           EDIT CAR
# *********************************************

@app.route("/edit/<int:id>")
def edit_cars_info(id):
    if "user_id" not in session:
        flash("Must be logged in")
        return redirect ("/")
    else:
        data = {
        "id" : id
        }
    artist_painting = Car.get_cars(data)
    return render_template("editcar.html", painting = artist_painting)


@app.route("/updatecar/<int:id>", methods = ["POST"])
def update_car(id):
    if Car.validate_car(request.form):
        data = {
            "id": id,
            "price": float(request.form["price"]),
            "model": request.form["model"],
            "make": request.form["make"],
            "year": request.form["year"],
            "description": request.form["description"],
            "user_id": session["user_id"]
        }
        Car.update_carinfo(data)
        return redirect("/dashboard")
    else:
        return redirect(f"/edit/{id}")


# *********************************************
#              DELETE ROUTE
# *********************************************

@app.route("/delete/<int:id>")
def delete(id):
    if "user_id" not in session:
        flash("Must be logged in")
        return redirect ("/")
    else:
        data = {
        "car_id" : id
        }
        Car.delete_car(data)
        return redirect("/dashboard")

# *********************************************
#              PURCHASED CARS
# *********************************************

@app.route("/purchasedcar/<int:id>")
def purchased_car(id):
    if "user_id" not in session:
        flash("Must be logged in")
        return redirect ("/")
    else:
        data = {
            "car_id": id,
            "user_id" : session["user_id"]
        }
        Car.insert_purchased_car(data)
        artist_painting = Car.get_cars_user_id(data)
        return redirect("/dashboard",purchased = artist_painting )
