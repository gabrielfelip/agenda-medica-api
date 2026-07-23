import app.routes as routes


def autenticar_usuario(client):

    resposta = client.post(
        "/login",
        json={
            "email": "teste@email.com",
            "senha": "123456"
        }
    )

    dados = resposta.get_json()

    return dados["token"]



def test_buscar_agendamentos_com_token(client, monkeypatch):


    dados_mock = [

        {
            "paciente": "Carlos Oliveira",
            "cpf": "123.456.789-00",
            "medico": "Dr. João Silva",
            "especialidade": "Cardiologia",
            "data": "25/07/2026",
            "horario": "08:30",
            "convenio": "Unimed",
            "status": "Confirmado"
        }

    ]


    monkeypatch.setattr(
        routes,
        "buscar_agendamentos",
        lambda: dados_mock
    )


    token = autenticar_usuario(client)


    resposta = client.get(
        "/agendamentos",
        headers={
            "Authorization": "Bearer " + token
        }
    )


    assert resposta.status_code == 200


    dados = resposta.get_json()


    assert len(dados) == 1

    assert dados[0]["paciente"] == "Carlos Oliveira"





def test_falha_api_agendamentos(client, monkeypatch):


    monkeypatch.setattr(
        routes,
        "buscar_agendamentos",
        lambda: {
            "erro": "Não foi possível conectar com a API"
        }
    )


    token = autenticar_usuario(client)


    resposta = client.get(
        "/agendamentos",
        headers={
            "Authorization": "Bearer " + token
        }
    )


    assert resposta.status_code == 503


    dados = resposta.get_json()


    assert "erro" in dados