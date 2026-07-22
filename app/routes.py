from flask import Blueprint, jsonify, request
from .database import db
from .models import Paciente


main = Blueprint("main", __name__)


@main.route("/")
def home():
    return jsonify({
        "message": "Agenda Médica API funcionando!"
    })


@main.route("/health")
def health():
    return jsonify({
        "status": "API online"
    })


@main.route("/pacientes", methods=["GET"])
def listar_pacientes():
    pacientes = Paciente.query.all()

    return jsonify([
        {
            "id": paciente.id,
            "nome": paciente.nome,
            "email": paciente.email,
            "telefone": paciente.telefone
        }
        for paciente in pacientes
    ])


@main.route("/pacientes", methods=["POST"])
def criar_paciente():

    dados = request.json

    paciente = Paciente(
        nome=dados["nome"],
        email=dados.get("email"),
        telefone=dados.get("telefone")
    )

    db.session.add(paciente)
    db.session.commit()

    return jsonify({
        "message": "Paciente criado com sucesso!",
        "id": paciente.id
    }), 201


@main.route("/pacientes/<int:id>", methods=["GET"])
def buscar_paciente(id):

    paciente = Paciente.query.get(id)

    if not paciente:
        return jsonify({
            "message": "Paciente não encontrado"
        }), 404

    return jsonify({
        "id": paciente.id,
        "nome": paciente.nome,
        "email": paciente.email,
        "telefone": paciente.telefone
    })

@main.route("/pacientes/<int:id>", methods=["PUT"])
def atualizar_paciente(id):

    paciente = Paciente.query.get(id)

    if not paciente:
        return jsonify({
            "message": "Paciente não encontrado"
        }), 404

    dados = request.json

    paciente.nome = dados.get("nome", paciente.nome)
    paciente.email = dados.get("email", paciente.email)
    paciente.telefone = dados.get("telefone", paciente.telefone)

    db.session.commit()

    return jsonify({
        "message": "Paciente atualizado com sucesso!"
    })

@main.route("/pacientes/<int:id>", methods=["DELETE"])
def deletar_paciente(id):

    paciente = Paciente.query.get(id)

    if not paciente:
        return jsonify({
            "message": "Paciente não encontrado"
        }), 404

    db.session.delete(paciente)
    db.session.commit()

    return jsonify({
        "message": "Paciente removido com sucesso!"
    })