import os

from flask import Flask, jsonify
from sqlalchemy.exc import OperationalError

from .routes import main
from .database import db
from .auth import auth

from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
load_dotenv()

os.makedirs("instance", exist_ok=True)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv(
    "JWT_SECRET_KEY",
    "jwt-secret-key"
)

database_url = os.getenv(
    "DATABASE_URL",
    "sqlite:///instance/agenda.db"
)

if database_url.startswith("sqlite:///"):

    db_path = database_url.replace(
        "sqlite:///",
        ""
    )

    db_path = os.path.abspath(db_path)
    database_url = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_DATABASE_URI"] = database_url

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

# Tratamento de erro de conexão com banco
@app.errorhandler(OperationalError)
def erro_banco(e):
    return jsonify({
        "erro": "Erro de conexão com o banco de dados"
    }), 500

# Criação das tabelas
with app.app_context():
    try:
        db.create_all()
    except OperationalError as erro:
        print(
            "Erro ao conectar com o banco de dados:",
            erro
        )