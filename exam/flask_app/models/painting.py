from flask import flash,request
import re

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

class Painting:
    def __init__(self,data):
        self.id = data["id"]
        self.title = data["title"]
        self.description = data["description"]
        self.price = data["price"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["id"]

# ********************************************
#          INSERST PAINTINGS INFO METHODS
# ********************************************

    @classmethod
    def insert_paintings(cls,data):
        query = "INSERT INTO paintings (title, description, price, user_id) VALUES (%(title)s, %(description)s, %(price)s, %(user_id)s)"
        return connectToMySQL("artists_and_paintings").query_db(query, data)


# ********************************************
#       VALIDATE PAINTINGS INFO METHODS
# ********************************************

    @staticmethod
    def validate_painting(painting):
        painting_valide = True
        if len(painting["title"]) < 2:
            flash("The Title Must be at least 2 characters long")
            painting_valide = False
        if len(painting["description"]) < 10:
            flash("The Description Must be at least 10 characters long")
            painting_valide = False
        if  painting["price"] == "":
            flash("The price Must be include")
            painting_valide = False
        if  painting["price"] == "0":
            flash("The price Must be greater than 0")
            painting_valide = False
        return painting_valide


# ********************************************
#             GET PAINTING
# ********************************************

    @classmethod
    def get_painting(cls, data):
        query = "SELECT * FROM paintings WHERE paintings.id = %(id)s "
        artist_painting = connectToMySQL("artists_and_paintings").query_db(query,data)
        return Painting(artist_painting[0])

# ********************************************
#             GET PAINTING
# ********************************************

    @classmethod
    def get_painting_user(cls, data):
        query = "SELECT * FROM users JOIN paintings  ON  paintings.user_id = users.id WHERE paintings.id= %(id)s  "
        artist_painting = connectToMySQL("artists_and_paintings").query_db(query,data)
        return User(artist_painting[0])


# ********************************************
#             DELETE PAINTING
# ******************************************** 

    @classmethod
    def delete_paintings(cls, data):
        query = "DELETE FROM paintings WHERE paintings.id = %(user_id)s"
        return  connectToMySQL("artists_and_paintings").query_db(query,data)

# ********************************************
#             UPDATE PAINTING
# ******************************************** 

    @classmethod
    def update_paintings(cls, data):
        query = "UPDATE paintings SET title = %(title)s, description = %(description)s, price = %(price)s WHERE  paintings.id = %(id)s"
        return  connectToMySQL("artists_and_paintings").query_db(query,data)

# ********************************************
#       DISPLAY ALL PAINTING AND ARTISTS 
# ********************************************

    @classmethod
    def get_artist_painting(cls):
        query = "SELECT * FROM users JOIN paintings ON paintings.user_id = users.id"
        db_painting = connectToMySQL("artists_and_paintings").query_db(query)
        artist_painting = []
        for ap in db_painting:
            artist_instance = User(ap)
            painting_data = {
                "id": ap["paintings.id"],
                "title": ap["title"],
                "description": ap["description"],
                "price": ap["price"],
                "created_at" : ap["created_at"],
                "updated_at" : ap["updated_at"]
            }
            artist_instance.painting = Painting(painting_data)
            artist_painting.append(artist_instance)
        return artist_painting

# ********************************************
#      DISPLAY USER PAINTING INFO METHODS
# ********************************************

    # @classmethod
    # def display_user_painting (cls, data):
    #     query = "SELECT * FROM users JOIN paintings ON paintings.id = %(user_id)s   "
    #     db_painting = connectToMySQL("artists_and_paintings").query_db(query, data)
    #     artist_painting = []
    #     for ap in db_painting:
    #         artist_instance = User(ap)
    #         painting_data = {
    #             "id": ap["paintings.id"],
    #             "title": ap["title"],
    #             "description": ap["description"],
    #             "price": ap["price"],
    #             "created_at" : ap["created_at"],
    #             "updated_at" : ap["updated_at"]
    #         }
    #         artist_instance.painting = Painting(painting_data)
    #         artist_painting.append(artist_instance)
    #     return artist_painting