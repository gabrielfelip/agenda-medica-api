from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from .database import db
from .models import Paciente
from flask_jwt_extended import jwt_required, get_jwt_identity
from .services.agenda_service import buscar_agendamentos


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
@jwt_required()
def listar_pacientes():

    usuario_id = get_jwt_identity()

    pacientes = Paciente.query.filter_by(
        usuario_id=usuario_id
    ).all()

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
@jwt_required()
def criar_paciente():

    dados = request.json

    if not dados.get("nome"):
        return jsonify({
            "message": "Nome é obrigatório"
        }), 400


    usuario_id = get_jwt_identity()

    paciente = Paciente(
        nome=dados["nome"],
        email=dados.get("email"),
        telefone=dados.get("telefone"),
        usuario_id=usuario_id
    )


    try:
        db.session.add(paciente)
        db.session.commit()

    except IntegrityError:
        db.session.rollback()

        return jsonify({
            "message": "Email já cadastrado"
        }), 400


    return jsonify({
        "message": "Paciente criado com sucesso!",
        "id": paciente.id
    }), 201



@main.route("/pacientes/<int:id>", methods=["GET"])
@jwt_required()
def buscar_paciente(id):

    usuario_id = get_jwt_identity()

    paciente = Paciente.query.filter_by(
        id=id,
        usuario_id=usuario_id
    ).first()


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
@jwt_required()
def atualizar_paciente(id):

    usuario_id = get_jwt_identity()

    paciente = Paciente.query.filter_by(
        id=id,
        usuario_id=usuario_id
    ).first()


    if not paciente:
        return jsonify({
            "message": "Paciente não encontrado"
        }), 404


    dados = request.json


    paciente.nome = dados.get(
        "nome",
        paciente.nome
    )

    paciente.email = dados.get(
        "email",
        paciente.email
    )

    paciente.telefone = dados.get(
        "telefone",
        paciente.telefone
    )


    db.session.commit()


    return jsonify({
        "message": "Paciente atualizado com sucesso!"
    })



@main.route("/pacientes/<int:id>", methods=["DELETE"])
@jwt_required()
def deletar_paciente(id):

    usuario_id = get_jwt_identity()

    paciente = Paciente.query.filter_by(
        id=id,
        usuario_id=usuario_id
    ).first()


    if not paciente:
        return jsonify({
            "message": "Paciente não encontrado"
        }), 404


    db.session.delete(paciente)
    db.session.commit()


    return jsonify({
        "message": "Paciente removido com sucesso!"
    })

@main.route("/agendamentos", methods=["GET"])
@jwt_required()
def listar_agendamentos():

    resultado = buscar_agendamentos()

    if isinstance(resultado, dict) and "erro" in resultado:
        return jsonify(resultado), 503


    if not resultado:
        return jsonify({
            "message": "Nenhum agendamento encontrado"
        }), 404


    return jsonify(resultado)