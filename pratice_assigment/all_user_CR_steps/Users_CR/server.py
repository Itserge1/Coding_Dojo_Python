from flask import Flask,render_template,request,redirect,session
from userinfo import Userinfo
# from flask.globals import session
# remenber MVC M(Model: is whatever files is communicating with you database . in our case it is userinfo.py ) V(View: is what we see the stuff tha is render to the page) C(Controler: is  the middle men between M an V. it grab the data and sent it to the model. it basical your servers)
app = Flask(__name__)
# app.secret_key = "keepitsecret"

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 5001, debug=True)