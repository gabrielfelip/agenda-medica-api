# Agenda Médica API

Sistema de gerenciamento de agenda médica desenvolvido em Python utilizando Flask, SQLite, Docker e integração com API HTTP.

A aplicação permite autenticação de usuários, gerenciamento de pacientes e consulta de agendamentos médicos através de uma API simulada, seguindo uma arquitetura organizada e separando responsabilidades entre autenticação, banco de dados, regras de negócio e integração externa.

---

## Sobre o projeto

O Agenda Médica API foi desenvolvido como solução para um desafio técnico de desenvolvimento backend.

O sistema possui:

- Autenticação de usuários utilizando JWT;
- Banco de dados SQLite para persistência das informações;
- Cadastro e consulta de pacientes;
- Integração com uma API simulada de agendamentos médicos;
- Tratamento de erros de comunicação;
- Ambiente preparado para execução utilizando Docker Compose.

---

## Tecnologias utilizadas

- Python 3.11
- Flask
- Flask SQLAlchemy
- Flask JWT Extended
- Flask Bcrypt
- SQLite
- Requests
- Pytest
- Docker
- Docker Compose

---

## Funcionalidades

- Cadastro de usuários;
- Login com autenticação JWT;
- Proteção de rotas autenticadas;
- Cadastro de pacientes;
- Consulta de pacientes vinculados ao usuário autenticado;
- Consulta de agendamentos médicos;
- Integração HTTP com API simulada;
- Tratamento de falhas de comunicação;
- Testes automatizados.

---

## Estrutura do projeto

```bash
agenda-medica/
│
├── app/
│   ├── auth.py
│   ├── database.py
│   ├── models.py
│   ├── routes.py
│   ├── seed.py
│   └── services/
│       └── agenda_service.py
│
├── mock_api/
│   ├── app.py
│   ├── data.json
│   ├── Dockerfile
│   └── requirements.txt
│
├── tests/
│   ├── conftest.py
│   └── test_auth.py
│
├── instance/
│   └── agenda.db
│
├── Dockerfile
├── docker-compose.yml
├── pytest.ini
├── requirements.txt
└── run.py
```

## Como executar o projeto localmente
### 1. Clone o repositório:
```bash
git clone https://github.com/gabrielfelip/agenda-medica-api.git
```
### 2. Acesse a pasta do projeto:
```bash
cd agenda-medica-api
```
### 3. Crie o ambiente virtual:
```bash
python -m venv .venv
```
### 4. Ative o ambiente virtual:
### Windows
```bash
.venv\Scripts\activate
```
### 5. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Criando usuário de teste
### Para criar automaticamente o usuário inicial do sistema:
```bash
python -m app.seed
```
### Credenciais:
```bash
Email:
usuario@email.com

Senha:
123456
```

## Executando a aplicação
### Execute:
```bash
python run.py
```
## A API ficará disponível em:

```bash
http://127.0.0.1:5000
```

## Executando com Docker
### A aplicação possui dois serviços:
- API principal Flask;
- API simulada de agendamentos.

### Para iniciar os serviços:
```bash

docker compose up --build
```

## Após a inicialização:

### API principal:
```bash
http://127.0.0.1:5000
```

## Mock API:
```bash
http://127.0.0.1:5001
```
## Exemplos de utilização

## Login

Endpoint:
```bash
POST /login
```
```bash

Exemplo:

{
    "email": "usuario@email.com",
    "senha": "123456"
}
```

### Retorno:
```bash

{
    "message": "Login realizado com sucesso!",
    "token": "JWT_TOKEN"
}
```

### Consultar agendamentos
### Endpoint:
```bash
GET /agendamentos
```
### Necessário enviar o token JWT:
```bash
Authorization: Bearer TOKEN
```

### Exemplo de resposta:
```bash
[
    {
        "convenio": "Unimed",
        "cpf": "123.456.789-00",
        "data": "25/07/2026",
        "especialidade": "Cardiologia",
        "horario": "08:30",
        "medico": "Dr. João Silva",
        "paciente": "Carlos Oliveira",
        "status": "Confirmado"
    }
]
```

## Cadastro de paciente
## Endpoint:
```bash
POST /pacientes
```
## Exemplo:
```bash

{
    "nome": "Carlos Oliveira",
    "email": "carlos@email.com",
    "telefone": "11999999999"
}
```

## Testes automatizados
### Os testes foram desenvolvidos utilizando Pytest.
### Executar:
```bash
pytest
```
## Testes implementados:
- Login com credenciais válidas;
- Login com credenciais inválidas;
- Validação de autenticação.

## Tratamento de erros
### A aplicação possui tratamento para:

- Usuário inexistente;
- Senha inválida;
- Campos obrigatórios ausentes;
- API externa indisponível;
- Timeout de comunicação;
- Resposta inválida da API;
- Nenhum agendamento encontrado.


## Decisões técnicas
- Flask foi escolhido pela simplicidade e adequação ao escopo do projeto.
- SQLite foi utilizado por ser um banco leve e suficiente para a aplicação proposta.
- JWT foi utilizado para autenticação e proteção das rotas.
- A API de agendamentos foi criada como um serviço separado para simular uma integração externa.
- Docker Compose foi utilizado para facilitar a execução de múltiplos serviços.
- A aplicação foi organizada separando autenticação, modelos, rotas e serviços.

## Limitações conhecidas
- A API simulada utiliza dados estáticos armazenados em JSON.
- O banco SQLite foi escolhido visando simplicidade e facilidade de execução.
- Não foi desenvolvido frontend completo, pois o foco principal do desafio foi backend, integração e arquitetura da aplicação.



