from flask import flash,request
import re

from flask_app.config.mysqlconnection import connectToMySQL


# ***************************************************************************************
# VALIDATE USER (CREATING THE CLASS AND ALL THE METHODE NEEDED FOR THE USER'S VALIDATION)
# *************************************************************************************** 

class User:
    def __init__(self,data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.id = data["id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.paintings = []

# ********************************************
#          INSERST USER INFO METHODS
# ********************************************

    @classmethod
    def insert_user(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        return connectToMySQL("artists_and_paintings").query_db(query, data)

# ********************************************
#          CHECK EXISTING USERS
# ********************************************

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        user_db = connectToMySQL("artists_and_paintings").query_db(query, data)

        if len(user_db) < 1:
            return False
        
        return cls(user_db[0])


# ********************************************
#          GET USERS
# ********************************************

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        user_db = connectToMySQL("artists_and_paintings").query_db(query, data)

        if len(user_db) < 1:
            return False
        
        return cls(user_db[0])


    # ********************************************
    #      VALIDATE USER INFO ROUTE METHODS
    # ********************************************
    #we pass in a parameter "user(that we name)" because we want to pass all the info that we recive from the user AKA "request.form"
    @staticmethod
    def validate_user(user):
        email_reg = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        first_name_reg = re.compile(r'[a-zA-Z]+$')
        last_name_reg =  re.compile(r'[a-zA-Z]+$')
        
        is_valid = True
        # this basicaly set the form to be true AKA "ok to pass", then we set a buch of condition and i on of those conditions failed the we set it to be is_valide = false therefoer no login(plus we flash our message)
        if  not first_name_reg.match(user["first_name"]):
            flash("Invalid First Name (name need to be only letters and at leaste 2 characters)")
            is_valid = False
        if  not last_name_reg.match(user["last_name"]):
            flash("Invalid Last Name (name need to be only letters and at leaste 2 characters)")
            is_valid = False
        if  not email_reg.match(user["email"]):
            flash("Invalid Email")
            is_valid = False
        else:
            data ={
                "email": request.form["email"],
            }
            query = "SELECT * FROM users WHERE email = %(email)s"
            email_check = connectToMySQL("artists_and_paintings").query_db(query, data)
            if len(email_check) >0:
                flash("Existing email")
                is_valid = False
        if len(user["password"]) < 8:
            flash("password has to be at least 2 characters")
            is_valid = False
        if (user["confirm_password"] != user["password"]):
            flash("Password has to be the same")
            is_valid = False
        if "checkbox" not in user:
            # a checkbox  will only exist in request.form AKA "user" only if the user checked it. So to created a condition on it, we just check if it is in request.form AKA "user" AKA the data reicive from the user input 
            flash ("check the checkbox")
            is_valid = False
        return is_valid

