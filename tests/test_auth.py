def test_login_sucesso(client):

    resposta = client.post(
        "/login",
        json={
            "email": "teste@email.com",
            "senha": "123456"
        }
    )


    assert resposta.status_code == 200

    dados = resposta.get_json()

    assert "token" in dados



def test_login_senha_invalida(client):

    resposta = client.post(
        "/login",
        json={
            "email": "teste@email.com",
            "senha": "senhaerrada"
        }
    )


    assert resposta.status_code == 401

def test_acessar_pacientes_sem_token(client):

    resposta = client.get(
        "/pacientes"
    )

    assert resposta.status_code == 401

    dados = resposta.get_json()

    assert "msg" in dados