from mysqlconnection import connectToMySQL

class Meme:
    @classmethod
    def insert_meme(cls,data):
        query = "INSERT INTO meme (name,meme_url) VALUES(%(name)s,%(meme_url)s)"
