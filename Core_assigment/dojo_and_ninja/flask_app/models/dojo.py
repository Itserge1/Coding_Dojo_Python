from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.name = data["name"]
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.dojo_id = data["dojo_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def insert_ninja(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUE (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)"
        return connectToMySQL("dojo_and_ninja").query_db(query,data)
    @classmethod
    def get_ninja(cls,data):
        query = "SELECT * FROM ninjas JOIN dojos ON dojo_id = dojos.id WHERE dojo_id = %(id)s"
        ninja_db = connectToMySQL("dojo_and_ninja").query_db(query,data)
        ninjas = []

        for ninja in ninja_db:
            print(ninja)
            ninjas.append(Ninja(ninja))
        return ninjas

class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    @classmethod
    def insert_dojo(cls,data):
        query = "INSERT INTO dojos (name) VALUE (%(name)s)"
        return connectToMySQL("dojo_and_ninja").query_db(query,data)
    @classmethod
    def get_dojo(cls):
        query = "SELECT * FROM dojos"
        db_dojo =  connectToMySQL("dojo_and_ninja").query_db(query)
        dojos =[]

        for dojo in db_dojo:
            dojos.append(Dojo(dojo))
        return dojos


