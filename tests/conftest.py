import pytest

from app import app
from app.database import db
from app.models import Usuario
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()


@pytest.fixture
def client():

    app.config["TESTING"] = True

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():

        db.create_all()

        senha_hash = bcrypt.generate_password_hash(
            "123456"
        ).decode("utf-8")


        usuario = Usuario(
            nome="Teste",
            email="teste@email.com",
            senha_hash=senha_hash
        )

        db.session.add(usuario)
        db.session.commit()


        yield app.test_client()


        db.session.remove()
        db.drop_all()