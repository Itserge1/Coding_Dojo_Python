from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html", num=3 , color= "green")


@app.route('/play')
def play():
    return render_template("index.html", num=3 , color= "green")

@app.route('/play/<int:num>')
def custum_play(num):
    return render_template("index.html",num= num, color= "green")

@app.route('/play/<int:num>/<string:color>')
def color_custum_play(num, color):
    return render_template("index.html",num= num,color = color)



if __name__=="__main__":
    app.run(host="0.0.0.0", port= 5001, debug=True)