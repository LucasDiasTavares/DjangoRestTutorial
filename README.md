# Django Rest Tutorial
Django Rest Tutorial entendendo o básico e criando uma API simpltes de pontos turísticos.

[Django Rest Framework Docs](https://www.django-rest-framework.org/).

## Pontos abordados na API

- Propor um novo produto - Qualquer pessoa.
- Moderação dos produtos cadastrados - Administradores da API.
- Listagem básica dos produtos (Lista resumida) - Via token.
- Listagem completa dos produtos - Via token.
- Detalhe de um produto - Via token.
- Atualização de um produto por usuários autorizados - Via token (Permissão especial)
- Deleção de um produto por usuários autorizados - Via token (Permissão especial)

## Endpoints da API
- 

## Requerimentos
- 

## Testando a minha API
#### Instalando a API
- Crie um novo ambiente virtual (env) e ative o mesmo
  - python3 -m venv nomeDoAmbiente
  - . nomeDoAmbiente/bin/activate

- Clone o meu projeto do github
  -  `git clone 'https://github.com/Pancitopenico/DjangoRestTutorial'`

- Instalando os requerimentos da API
  - pip install -r requirements-dev.txt
  
- Instalando primeiros passos
  - python manage.py makemigrations
  - python manage.py migrate
  - python manage.py createsuperuser
  - python manage.py runserver
  
- Agora provavelmente tudo irá rodar perfeitamente