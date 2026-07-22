from flask import Blueprint, jsonify, request
from .database import db
from .models import Usuario
from flask_bcrypt import Bcrypt


auth = Blueprint("auth", __name__)

bcrypt = Bcrypt()


@auth.route("/register", methods=["POST"])
def registrar_usuario():

    dados = request.json

    if not dados.get("nome"):
        return jsonify({
            "message": "Nome é obrigatório"
        }), 400

    if not dados.get("email"):
        return jsonify({
            "message": "Email é obrigatório"
        }), 400

    if not dados.get("senha"):
        return jsonify({
            "message": "Senha é obrigatória"
        }), 400


    senha_hash = bcrypt.generate_password_hash(
        dados["senha"]
    ).decode("utf-8")


    usuario = Usuario(
        nome=dados["nome"],
        email=dados["email"],
        senha_hash=senha_hash
    )


    db.session.add(usuario)
    db.session.commit()


    return jsonify({
        "message": "Usuário criado com sucesso!",
        "id": usuario.id
    }), 201



@auth.route("/login", methods=["POST"])
def login_usuario():

    dados = request.json

    if not dados.get("email") or not dados.get("senha"):
        return jsonify({
            "message": "Email e senha são obrigatórios"
        }), 400


    usuario = Usuario.query.filter_by(
        email=dados["email"]
    ).first()


    if not usuario:
        return jsonify({
            "message": "Usuário não encontrado"
        }), 404


    senha_valida = bcrypt.check_password_hash(
        usuario.senha_hash,
        dados["senha"]
    )


    if not senha_valida:
        return jsonify({
            "message": "Senha inválida"
        }), 401


    return jsonify({
        "message": "Login realizado com sucesso!",
        "usuario": {
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email
        }
    })