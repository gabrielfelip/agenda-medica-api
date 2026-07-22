# Agenda Médica API

Sistema de gerenciamento de consultas médicas desenvolvido em Python, com integração de API, banco de dados e ambiente Docker.

## Sobre o projeto

O Agenda Médica API é uma aplicação criada para gerenciar consultas médicas, permitindo autenticação de usuários, cadastro e consulta de informações de agenda.

O projeto utiliza uma arquitetura simples e organizada, separando responsabilidades entre autenticação, banco de dados, modelos e integração com serviços externos simulados.

## Tecnologias utilizadas

- Python
- Flask
- SQLite
- REST API
- Docker
- Docker Compose
- HTML/CSS
- Jinja Templates

## Funcionalidades

- Sistema de login de usuários
- Gerenciamento de consultas médicas
- Cadastro e consulta de dados
- Integração com API externa simulada
- Persistência de informações em banco de dados
- Ambiente configurado com Docker

## Estrutura do projeto
```bash
agenda-medica/
│
├── app/
│   ├── api_client.py
│   ├── auth.py
│   ├── database.py
│   ├── models.py
│   └── templates/
│
├── mock_api/
│   ├── app.py
│   └── data.json
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── run.py
```

## Como executar o projeto

Clone o repositório:
```bash

git clone https://github.com/gabrielfelip/agenda-medica-api.git
```

Acesse a pasta:
```bash

cd agenda-medica-api
```

Crie um ambiente virtual:
```bash

python -m venv .venv
```

Ative o ambiente virtual:

Windows:
```bash

.venv\Scripts\activate
```

Instale as dependências:
```bash

pip install -r requirements.txt
```

Execute a aplicação:
```bash

python run.py
```

## Executando com Docker

Para executar utilizando Docker Compose:
```bash

docker-compose up --build
```

## Objetivo do projeto

Projeto desenvolvido com objetivo de praticar desenvolvimento backend utilizando Python, criação de APIs, integração entre serviços, banco de dados e containerização com Docker.

## Autor

Gabriel Silva

GitHub:
https://github.com/gabrielfelip