from flask.helpers import flash
from flask_app import app
from flask import render_template, redirect, request,session
from flask_app.models.painting import Painting
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# *********************************************
#              ADD PAINTINGS
# *********************************************

@app.route("/paintings/new")
def paintings():
    if "user_id" not in session:
        flash("Must be logged in")
        return redirect ("/")
    else:
        return render_template("newpaintings.html")

# *********************************************
#            INSERTS PAINTINGS
# *********************************************

@app.route("/insertpaintings", methods = ["POST"])
def insertpaintings():
    if Painting.validate_painting(request.form):
        data = {
                "title": request.form["title"],
                "description": request.form["description"],
                "price": request.form["price"],
                "user_id": session["user_id"]
            }
        Painting.insert_paintings(data)
        return redirect("/dashboard")
    else:
        return redirect("/paintings/new")

# *********************************************
#            SHOW PAINTING INFO  ROUTE
# *********************************************

@app.route("/paintings/<int:id>")
def painting_info(id):
    if "user_id" not in session:
        flash("Must be logged in")
        return redirect ("/")
    else:
        data = {
            "id":id
        }
        artist_painting = Painting.get_painting_user(data)
        pikabo = Painting.get_painting(data)
        return render_template("paintinginfo.html", painting = artist_painting , name = pikabo)

# *********************************************
#           SHOW PAINTING INFO  ROUTE
# *********************************************

@app.route("/paintings/<int:id>/edit")
def edit_painting_info(id):
    if "user_id" not in session:
        flash("Must be logged in")
        return redirect ("/")
    else:
        data = {
        "id" : id
        }
    artist_painting = Painting.get_painting(data)
    return render_template("editpaintinginfo.html", painting = artist_painting)


@app.route("/editpainting/<int:id>", methods = ["POST"])
def edit_painting(id):
    if Painting.validate_painting(request.form):
        data = {
                "id": id,
                "title": request.form["title"],
                "description": request.form["description"],
                "price": float(request.form["price"]),
                "user_id": session["user_id"]
            }
        Painting.update_paintings(data)
        return redirect("/dashboard")
    else:
        return redirect(f"/paintings/{id}/edit")


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
        "user_id" : id
        }
        Painting.delete_paintings(data)
        return redirect("/dashboard")