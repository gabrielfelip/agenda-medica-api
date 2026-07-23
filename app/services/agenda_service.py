import requests


API_URL = "http://mock_api:5001/agendamentos"


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

        return dados


    except requests.exceptions.Timeout:
        return {
            "erro": "A API demorou para responder"
        }


    except requests.exceptions.ConnectionError:
        return {
            "erro": "Não foi possível conectar com a API"
        }


    except requests.exceptions.RequestException:
        return {
            "erro": "Erro ao consultar API"
        }