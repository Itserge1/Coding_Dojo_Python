from flask_app import app
from flask_app.controllers import users
# from flask import Flask,render_template,request,redirect,session
# from userinfo import Userinfo
# # from flask.globals import session
# # remenber MVC M(Model: is whatever files is communicating with you database . in our case it is userinfo.py ) V(View: is what we see the stuff tha is render to the page) C(Controler: is  the middle men between M an V. it grab the data and sent it to the model. it basical your servers)
# app = Flask(__name__)
# # app.secret_key = "keepitsecret"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 5001, debug=True)