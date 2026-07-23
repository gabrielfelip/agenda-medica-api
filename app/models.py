from .database import db


class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True
    )

    telefone = db.Column(
        db.String(20)
    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuario.id"),
        nullable=False
    )

    def __repr__(self):
        return f"<Paciente {self.nome}>"


class Usuario(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    senha_hash = db.Column(
        db.String(200),
        nullable=False
    )

    pacientes = db.relationship(
        "Paciente",
        backref="usuario",
        lazy=True
    )

    agendamentos = db.relationship(
        "Agendamento",
        backref="usuario",
        lazy=True
    )

    def __repr__(self):
        return f"<Usuario {self.email}>"


class Agendamento(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    paciente = db.Column(
        db.String(100),
        nullable=False
    )

    cpf = db.Column(
        db.String(14),
        nullable=False
    )

    medico = db.Column(
        db.String(100),
        nullable=False
    )

    especialidade = db.Column(
        db.String(100),
        nullable=False
    )

    data = db.Column(
        db.String(20),
        nullable=False
    )

    horario = db.Column(
        db.String(20),
        nullable=False
    )

    convenio = db.Column(
        db.String(100),
        nullable=False
    )

    status = db.Column(
        db.String(50),
        nullable=False
    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuario.id"),
        nullable=False
    )

    def __repr__(self):
        return f"<Agendamento {self.paciente}>"