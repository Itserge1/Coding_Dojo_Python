from flask_app import app
from flask_app.controllers import users
from flask_app.controllers import recipies



if __name__ == "__main__":
    app.run(port=5001, debug=True)