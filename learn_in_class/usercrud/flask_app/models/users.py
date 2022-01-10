from flask_app.config.mysqlconnection import connectToMySQL


# *************************************************************
# CREATING A USER CLASS AND ITS METHODS TO MANIPULATE USER INFO
# *************************************************************
class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    @classmethod
    def insert_user(cls, data):
        query = "INSERT INTO Users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        return connectToMySQL("userscr_db").query_db(query,data)

    @classmethod
    def dispay_alluser(cls):
        query = "SELECT * FROM  Users ORDER BY Users.id DESC"
        db_user =  connectToMySQL("userscr_db").query_db(query)
        Users = []

        for user in db_user:
            Users.append(User(user))
        return Users

    @classmethod
    def dispay_user(cls,data):
        query = "SELECT * FROM  Users WHERE id = %(id)s "
        db_user =  connectToMySQL("userscr_db").query_db(query,data)
        Users = []

        for user in db_user:
            Users.append(User(user))
        return Users
    
    @classmethod
    def edit_user(cls,data):
        query = "SELECT * FROM  Users WHERE id = %(id)s "
        Users =  connectToMySQL("userscr_db").query_db(query,data)
        return cls(Users[0])

    @classmethod
    def real_edituser(cls, data):
        query = "UPDATE Users SET first_name=%(first_name)s, last_name=%(last_name)s,email=%(email)s WHERE id = %(id)s"
        return connectToMySQL("userscr_db").query_db(query,data)

    @classmethod
    def deleteuser(cls, data):
        query = "DELETE FROM Users WHERE id = %(id)s"
        return connectToMySQL("userscr_db").query_db(query,data)