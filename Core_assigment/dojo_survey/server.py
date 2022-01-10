from flask import Flask,render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = "keepitsecret"

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]
    return redirect("/result")

@app.route("/result")
def result():
    return render_template("result.html", name= session["name"], location= session["location"], language= session["language"], comment= session["comment"])

if __name__ == "__main__":
    app.run(debug = True)