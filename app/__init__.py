import os

from flask import Flask
from .routes import main
from .database import db
from .auth import auth

from flask_jwt_extended import JWTManager
from dotenv import load_dotenv


load_dotenv()


app = Flask(__name__)


app.config["JWT_SECRET_KEY"] = os.getenv(
    "JWT_SECRET_KEY",
    "jwt-secret-key"
)


app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "sqlite:///agenda.db"
)


print(
    "BANCO ATUAL:",
    app.config["SQLALCHEMY_DATABASE_URI"]
)


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


app.json.ensure_ascii = False


db.init_app(app)


jwt = JWTManager(app)


app.register_blueprint(main)
app.register_blueprint(auth)


with app.app_context():
    db.create_all()