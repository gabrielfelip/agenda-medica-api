from flask import Flask, jsonify
import json


app = Flask(__name__)


@app.route("/agendamentos", methods=["GET"])
def listar_agendamentos():

    with open("data.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return jsonify(dados)


@app.route("/health")
def health():

    return jsonify({
        "status": "Mock API online"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True
    )