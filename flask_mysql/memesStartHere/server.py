from flask import Flask, render_template,request,redirect
from meme import Meme
app = Flask(__name__)

@app.route("/")
def index():
    return  render_template("index.html")

@app.route("/insertmeme", method=["POST"])
def index_meme():
    data = {
        "name":request.form["name"],
        "meme_url":request.form["meme_url"]
    }
    Meme.indert_name(data)
    return redirect("?")

if __name__ == "__main__":
    app.run(debug=True)


