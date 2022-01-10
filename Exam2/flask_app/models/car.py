from flask import flash,request
import re

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

class Car:
    def __init__(self,data):
        self.id = data["id"]
        self.price = data["price"]
        self.model = data["model"]
        self.make = data["make"]
        self.year = data["year"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["id"]


# ********************************************
#          INSERST CARS INFO METHOD
# ********************************************

    @classmethod
    def insert_car(cls,data):
        query = "INSERT INTO cars (price, model, make, year, description, user_id) VALUES (%(price)s, %(model)s, %(make)s, %(year)s, %(description)s, %(user_id)s)"
        return connectToMySQL("user_and_car").query_db(query, data)

# ********************************************
#       VALIDATE CARS INFO METHOD
# ********************************************

    @staticmethod
    def validate_car(painting):
        painting_valide = True
        if  painting["price"] == "0":
            flash("The price Must be greater than 0")
            painting_valide = False
        if  painting["year"] == "0":
            flash("The year Must be greater than 0")
            painting_valide = False
        if  painting["price"] == "":
            flash("The price Must be include")
            painting_valide = False
        if  painting["year"] == "":
            flash("The year Must be include")
            painting_valide = False
        if painting["model"] =="":
            flash("The Model Must be include")
            painting_valide = False
        if painting["make"] =="":
            flash("The Original company Must be include")
            painting_valide = False
        if painting["description"] =="":
            flash("The Description Must be include")
            painting_valide = False
        return painting_valide


# ********************************************
#       DISPLAY ALL CARS AND SELLERS 
# ********************************************

    @classmethod
    def get_seller_car(cls):
        query = "SELECT * FROM users JOIN cars ON cars.user_id = users.id"
        db_painting = connectToMySQL("user_and_car").query_db(query)
        artist_painting = []
        for ap in db_painting:
            artist_instance = User(ap)
            painting_data = {
                "id": ap["cars.id"],
                "price": ap["price"],
                "model": ap["model"],
                "make": ap["make"],
                "year": ap["year"],
                "description": ap["description"],
                "created_at" : ap["created_at"],
                "updated_at" : ap["updated_at"]
            }
            artist_instance.cars = Car(painting_data)
            artist_painting.append(artist_instance)
        return artist_painting


# ********************************************
#             GET CARS
# ********************************************

    @classmethod
    def get_cars(cls, data):
        query = "SELECT * FROM cars WHERE cars.id = %(id)s "
        artist_painting = connectToMySQL("user_and_car").query_db(query,data)
        return Car(artist_painting[0])

# ********************************************
#             GET CARS AND USER
# ********************************************

    @classmethod
    def get_cars_user(cls, data):
        query = "SELECT * FROM users JOIN cars  ON  cars.user_id = users.id WHERE cars.id= %(id)s  "
        artist_painting = connectToMySQL("user_and_car").query_db(query,data)
        return User(artist_painting[0])


# ********************************************
#             DELETE CAR
# ******************************************** 

    @classmethod
    def delete_car(cls, data):
        query = "DELETE FROM cars WHERE cars.id = %(car_id)s"
        return  connectToMySQL("user_and_car").query_db(query,data)

# ********************************************
#             UPDATE CAR
# ******************************************** 

    @classmethod
    def update_carinfo(cls, data):
        query = "UPDATE cars SET price = %(price)s, model = %(model)s, make = %(make)s, year = %(year)s, description = %(description)s WHERE  cars.id = %(id)s"
        return  connectToMySQL("user_and_car").query_db(query,data)


# ********************************************
#      INSERST PURCHASED CARS INFO METHOD
# ********************************************

    @classmethod
    def insert_purchased_car(cls,data):
        query = "INSERT INTO cars_has_users (car_id, user_id) VALUES (%(car_id)s, %(user_id)s)"
        return connectToMySQL("user_and_car").query_db(query, data)

# ********************************************
#      GET PURCHASED CARS ID
# ********************************************

    @classmethod
    def get_cars_user_id(cls, data):
        query = "SELECT * FROM cars JOIN cars_has_users  ON  cars_has_users.car_id = %(car_id)s"
        artist_painting = connectToMySQL("user_and_car").query_db(query,data)
        return artist_painting