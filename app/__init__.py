from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
from flask_login import LoginManager

mysql = MySQL()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    CORS(app)

    mysql.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    from app.routes import main
    app.register_blueprint(main)

    return app