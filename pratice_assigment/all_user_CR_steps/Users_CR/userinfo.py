from mysqlconnection import connectToMySQL

class Userinfo:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
# the class methode bellow is going to insert all the info we recive from our form into our database
# to do so we first send somr SQL code in form of a string to our database(as done in line 19)
# we look for the keys  (first_nam, last_name, email) and insert there value in them (%(first_name)s, %(last_name)s, %(email)s), we also make sure to sanitize or data to avoid injection 
# an injection is when someone write some SQL code as an input in your website in orde for it to be trated as an SQL code instead on some normal text.
# the line 20 transfer all or data into or database. 
# if we run line 20 it will return an id number that will be the number of the row were all the info will be store at in or database.
    @classmethod
    def insert_userinfo(cls,data):
        query = "INSERT INTO Users (first_name,last_name,email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        return connectToMySQL("userscr_db").query_db(query,data)
# Remenber, select queries alway print the data as a list of dictionaries
    @classmethod
    def readalluser(cls):
        query = "SELECT * FROM Users ORDER BY Users.id DESC"
        db_users = connectToMySQL("userscr_db").query_db(query)
        Users = []
        for user in db_users:
            Users.append(Userinfo(user))
        return Users
    
    @classmethod
    def readuser(cls, data):
        query = "SELECT * FROM Users WHERE id = %(id)s"
        db_users = connectToMySQL("userscr_db").query_db(query,data)
        Users = []
        for user in db_users:
            Users.append(Userinfo(user))
        return Users
    
    @classmethod
    def edituser(cls, data):
        query = "SELECT * FROM Users WHERE id = %(id)s"
        Users = connectToMySQL("userscr_db").query_db(query,data)
        return cls (Users[0])
    
    @classmethod
    def deleteuser(cls, data):
        query = "DELETE FROM Users WHERE id = %(id)s"
        return connectToMySQL("userscr_db").query_db(query,data)
    
    @classmethod
    def real_edituser(cls, data):
        query = "UPDATE Users SET first_name=%(first_name)s, last_name=%(last_name)s,email=%(email)s WHERE id = %(id)s"
        return connectToMySQL("userscr_db").query_db(query,data)