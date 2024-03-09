from flask import Flask
from pymongo import MongoClient
import os
from flask_login import LoginManager
from .database import init_db






def create_app(test_config=None):
    
     
        


    app = Flask(__name__)
    app.config['SECRET_KEY'] = "abcdefg"
    
    app.config['TESTING'] = test_config is not None

    init_db(app)



    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_prefix = "/")


    from .models import User

    

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User(id) 


    return app




