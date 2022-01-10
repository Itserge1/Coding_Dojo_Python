from flask import flash,request,session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
class Recipe:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instruction = data["instructions"]
        self.date = data["date"]
        self.time = data["time"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]


# ********************************************
#          INSERST RECIPIES INFO METHODS
# ********************************************

    @classmethod
    def insert_recipies(cls,data):
        query = "INSERT INTO recipies (name, description, instructions, date, time, user_id) VALUES (%(name)s, %(description)s, %(instruction)s, %(date)s, %(time)s, %(user_id)s)"
        return connectToMySQL("recipies").query_db(query, data)

# ********************************************
#      DISPLAY USER RECIPIE INFO METHODS
# ********************************************

    @classmethod
    def display_user_recipies(cls, data):
        query = "SELECT * FROM recipies WHERE recipies.id = %(user_id)s "
        db_recipies = connectToMySQL("recipies").query_db(query,data)
        Recipies = []
        for recipie in db_recipies:
            Recipies.append(Recipe(recipie))
        return Recipies

# ********************************************
#             GET ALL RECIPIES 
# ********************************************

    @classmethod
    def get_recipies(cls, data):
        query = "SELECT * FROM recipies WHERE recipies.id = %(user_id)s "
        return  connectToMySQL("recipies").query_db(query,data)

# ********************************************
#      DISPLAY ALL RECIPIES ON DASHBOARD
# ********************************************

    @classmethod
    def display_recipies(cls):
        query = "SELECT * FROM recipies "
        db_recipies = connectToMySQL("recipies").query_db(query)
        Recipies = []
        for recipie in db_recipies:
            Recipies.append(Recipe(recipie))
        return Recipies
        # query = "SELECT * FROM users JOIN recipies ON recipies.user_id = users.id"
        # db_users_recipies = connectToMySQL("recipies").query_db(query)
        # Recipies = []
        # for recipie in db_users_recipies:
        #     user_instance = User(recipie)
        #     recipie_data = {
        #         "id": recipie["id"],
        #         "name": recipie["name"],
        #         "description": recipie["description"],
        #         "instructions": recipie["instructions"],
        #         "date": recipie["date"],
        #         "time": recipie["time"],
        #         "created_at": recipie["created_at"],
        #         "updated_at": recipie["updated_at"]
        #     }
        #     user_instance.recipie = Recipe(recipie_data)
        #     Recipies.append(user_instance)
        # return Recipies

# ********************************************
#            RECIPIES UPDATE
# ********************************************

    @classmethod
    def update_recipies(cls, data):
        query = "UPDATE recipies SET name = %(name)s, description = %(description)s, instructions = %(instruction)s, date = %(date)s, time = %(time)s WHERE  recipies.id = %(user_id)s"
        return  connectToMySQL("recipies").query_db(query,data)


# ********************************************
#       VALIDATE RECEPIES INFO METHODS
# ********************************************


    @staticmethod
    def validate_recipie(recipie):
        recipe_valide = True
        
        if len(recipie["name"]) < 3:
            flash("The recipie Must be 3 characters long")
            recipe_valide = False
        if len(recipie["description"]) < 3:
            flash("The recipie Must be 3 characters long")
            recipe_valide = False
        if len(recipie["instruction"]) < 3:
            flash("The recipie Must be 3 characters long")
            recipe_valide = False
        if "date" not in recipie:
            flash("Date must be field")
            recipe_valide = False
        if "time" not in recipie:
            flash("Under 30 Minute must be field")
            recipe_valide = False
        return recipe_valide

