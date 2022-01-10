from flask.helpers import flash
from flask_app import app
from flask import render_template, redirect, request,session
from flask_app.models.user import User
from flask_app.models.recipie import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def hello():
    return render_template("/home.html")

# ********************************************
# VALIDATE/INSERST USER INFO REGISTER  ROUTE
# ********************************************

@app.route("/validateuser", methods=["POST"])
def validate_user():
    if User.validate_user(request.form):
        # if the condition above is true, then we run the code below, but if it is false then we run the code in the else part. But what makes it true or false? (the varialble "is_valide" set in the model "user.py" in the class "User" ,method validate_user(user))
        pw_hash = bcrypt.generate_password_hash(request.form["password"])
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "password": pw_hash
        }
        user_id = User.insert_user(data)
        session["first_name"] = request.form["first_name"]
        session["user_id"] = user_id
        return redirect("/dashboard")
    else:
        return redirect("/")


# *************************************************************
#      LOGIN ROUTE / CHECKING EXIXTING USER AND PUT IN SESSION
# *************************************************************

@app.route("/login", methods=["POST"])
def login():
    # if the condition above is true, then we run the code below, but if it is false then we run the code in the else part. But what makes it true or false? (the varialble "is_valide" set in the model "user.py" in the class "User" ,method validate_user(user))
    data = {
        "email": request.form["email"],
        "password": request.form["password"]
    }
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")

    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("Invalid Email/Password")
        return redirect("/")

    session["user_id"] = user_in_db.id
    session["first_name"] = user_in_db.first_name
    session["last_name"] = user_in_db.last_name

    return redirect("/dashboard")

# *********************************************
#              DASHBOARD ROUTE
# *********************************************

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Must be logged in")
        return redirect ("/")
    else:
        # data = {
        #     "user_id": session["user_id"]
        # }
        Recipies = Recipe.display_recipies()
        return render_template("dashboard.html", recipie = Recipies)


# *********************************************
#              LOGOUT ROUTE
# *********************************************

@app.route("/logout")
def logout():
    session.clear()
    flash("logged out")
    return render_template("/home.html")