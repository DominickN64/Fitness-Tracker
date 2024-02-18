from flask import Flask
from pymongo import MongoClient
import os
from flask_login import LoginManager
import certifi

MONGO_URI = os.getenv("MONGO_URI")

ca_cert_path = certifi.where()

cluster = MongoClient(MONGO_URI,tlsCAFile=ca_cert_path)

db = cluster["FitnessApp"]
collection = db["UserInfo"]



def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = "abcdefg"



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




