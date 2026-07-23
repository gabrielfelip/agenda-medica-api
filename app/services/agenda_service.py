import requests
import os


API_URL = os.getenv(
    "MOCK_API_URL",
    "http://127.0.0.1:5001/agendamentos"
)


CAMPOS_OBRIGATORIOS = [
    "paciente",
    "cpf",
    "medico",
    "especialidade",
    "data",
    "horario",
    "convenio",
    "status"
]


def buscar_agendamentos():

    try:

        resposta = requests.get(
            API_URL,
            timeout=5
        )


        resposta.raise_for_status()


        dados = resposta.json()


        if not isinstance(dados, list):

            return {
                "erro": "Resposta da API inválida"
            }


        if not dados:

            return {
                "erro": "Nenhum agendamento encontrado"
            }


        for agendamento in dados:

            for campo in CAMPOS_OBRIGATORIOS:

                if campo not in agendamento:

                    return {
                        "erro": f"Campo obrigatório ausente: {campo}"
                    }


        return dados



    except requests.exceptions.Timeout:

        return {
            "erro": "A API demorou para responder"
        }



    except requests.exceptions.ConnectionError:

        return {
            "erro": "Não foi possível conectar com a API"
        }



    except requests.exceptions.JSONDecodeError:

        return {
            "erro": "Resposta da API não está em formato JSON válido"
        }



    except requests.exceptions.RequestException:

        return {
            "erro": "Erro ao consultar API"
        }