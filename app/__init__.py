from flask import Flask
from .routes import main
from .database import db
from .auth import auth
from flask_jwt_extended import JWTManager


app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "chave-super-secreta-agenda-medica"

app.json.ensure_ascii = False


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///agenda.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)

jwt = JWTManager(app)


app.register_blueprint(main)
app.register_blueprint(auth)


with app.app_context():
    db.create_all()