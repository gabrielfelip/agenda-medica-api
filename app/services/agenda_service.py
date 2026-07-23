import os
import logging
import requests


logger = logging.getLogger(__name__)


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

        logger.info("Consultando API de agendamentos")

        resposta = requests.get(
            API_URL,
            timeout=5
        )

        resposta.raise_for_status()

        dados = resposta.json()


        if not isinstance(dados, list):

            logger.error(
                "Resposta da API inválida: esperado uma lista"
            )

            return {
                "erro": "Resposta da API inválida"
            }


        for agendamento in dados:

            for campo in CAMPOS_OBRIGATORIOS:

                if campo not in agendamento:

                    logger.error(
                        f"Campo obrigatório ausente na resposta da API: {campo}"
                    )

                    return {
                        "erro": f"Campo obrigatório ausente: {campo}"
                    }


        logger.info(
            f"{len(dados)} agendamentos carregados com sucesso"
        )

        return dados



    except requests.exceptions.Timeout:

        logger.warning(
            "Timeout ao consultar API de agendamentos"
        )

        return {
            "erro": "A API demorou para responder"
        }



    except requests.exceptions.ConnectionError:

        logger.error(
            "Não foi possível conectar com a API de agendamentos"
        )

        return {
            "erro": "Não foi possível conectar com a API"
        }



    except requests.exceptions.RequestException as erro:

        logger.exception(
            f"Erro ao consultar API: {erro}"
        )

        return {
            "erro": "Erro ao consultar API"
        }