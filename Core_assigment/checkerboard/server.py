from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html", numj=4, numi=4)

@app.route("/<int:numj>")
def custum_height(numj):
    return render_template("index.html", numj= numj, numi=6)

@app.route("/<int:numj>/<int:numi>")
def custum_num(numj, numi):
    return render_template("index.html",numj=numj, numi=numi)

@app.route("/<int:numj>/<int:numi>/<string:color1>")
def custum_color(numj, numi, color1):
    return render_template("index.html",numj=numj, numi=numi, color1=color1)

@app.route("/<int:numj>/<int:numi>/<string:color1>/<string:color2>")
def custum_numcolor(numj, numi, color1, color2):
    return render_template("index.html",numj=numj, numi=numi, color1=color1, color2= color2)

if __name__ == "__main__":
    app.run(debug=True)

