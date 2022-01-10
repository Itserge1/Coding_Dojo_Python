from flask import Flask,render_template,session,redirect
app = Flask(__name__)

app.secret_key = "Someone was here"

@app.route("/")
def counter():
    if "user" not in session:
        session["user"] = 0
    session["user"] += 1
    return render_template("index.html")

@app.route("/destroy_session")
def reset():
    session.clear()
    return redirect("/")

@app.route("/plus_two")
def plus_two():
    if "user" not in session:
        session["user"] = 0
    session["user"] += 2
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
