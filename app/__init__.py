from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from app.config import Config
from app.routes.auth.login import login_bp
from app.routes.auth.logout import logout_bp
from app.routes.auth.register import register_bp
from app.routes.home import home_bp
from app.routes.budget import budget_bp

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    login_manager.init_app(app)
    login_manager.login_view = 'login'

    app.register_blueprint(login_bp, url_prefix='/auth')
    app.register_blueprint(logout_bp, url_prefix='/auth')
    app.register_blueprint(register_bp, url_prefix='/auth')
    app.register_blueprint(budget_bp, url_prefix='/budget')
    app.register_blueprint(home_bp, url_prefix='/')

    return app

app = create_app()