from app import app
from app.database import db
from app.models import Usuario
from app.auth import bcrypt


with app.app_context():

    usuario_existente = Usuario.query.filter_by(
        email="usuario@email.com"
    ).first()


    if usuario_existente:
        print("Usuário de teste já existe!")

    else:

        senha_hash = bcrypt.generate_password_hash(
            "123456"
        ).decode("utf-8")


        usuario = Usuario(
            nome="Usuario Teste",
            email="usuario@email.com",
            senha_hash=senha_hash
        )


        db.session.add(usuario)
        db.session.commit()


        print("Usuário de teste criado com sucesso!")