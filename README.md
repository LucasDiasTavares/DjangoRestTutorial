# Django Rest Tutorial
##### Projeto em desenvolvimento
Django Rest Tutorial entendendo o básico e criando uma API simples de pontos turísticos.
[Django Rest Framework Docs](https://www.django-rest-framework.org/).

## Pontos abordados na API

- Propor um novo ponto turístico - Qualquer pessoa.
- Moderação dos pontos turísticos cadastrados - Administradores da API.
- Listagem básica dos pontos turísticos (Lista resumida) - Via token.
- Listagem completa dos pontos turisticos - Via token.
- Detalhe de um ponto turístico - Via token.
- Atualização de um ponto turístico por usuários autorizados - Via token (Permissão especial)
- Deleção de um ponto turístico por usuários autorizados - Via token (Permissão especial)

## Endpoints da API
#### Estes são os primeiros endpoints da minha API
- http://127.0.0.1:8000/ => (GET) Contém a lista de todos os endpoints.
- http://127.0.0.1:8000/api/pontos-turisticos/ => (GET) Listagem de todos os pontos turístico.
- http://127.0.0.1:8000/api/pontos-turisticos/ => (POST) Adiciona um novo ponto turístico.
- http://127.0.0.1:8000/api/pontos-turisticos/1/ => (GET) Mostra um ponto turístico apenas, sendo o número 1 o id do objeto.
- http://127.0.0.1:8000/api/pontos-turisticos/1/ => (PUT) Atualiza as informações do meu ponto turistico, sendo o número 1 o id do objeto.
- http://127.0.0.1:8000/api/pontos-turisticos/1/ => (DELETE) Deleta um ponto turístico apenas, sendo o número 1 o id do objeto.
#### Segue o mesmo padrão para os demais endpoints.
- http://127.0.0.1:8000/api/atracoes/
- http://127.0.0.1:8000/api/enderecos/
- http://127.0.0.1:8000/api/comentarios/
- http://127.0.0.1:8000/api/avaliacoes/

#### Endpoints especiais
Este endpoint foi criado para que eu consiga fazer a "Moderação dos pontos turisticos cadastrados".
- http://127.0.0.1:8000/api/pontos-turisticos-aprovados => (GET) Retorna todos os pontos turisticos aprovados.

Este endpoint foi criado para que eu consiga fazer uma ordenação nos meus resultados.
- http://127.0.0.1:8000/api/pontos-turisticos-nome/?nome=Ponto (GET) Retorna todos os pontos turisticos que contenha a palavra Ponto no nome em ordem alfabetica, caso não passe nada na variavel irá retornar todos os pontos turisticos.
- http://127.0.0.1:8000/api/atracoes/?nome=AlgoEscrito&descricao=AlgoEscrito (GET) Instalção do DjangoFilterBackend possibilitando que seja filtrado por nome e/ou descrição, porém ele está como exactly

## Alterações no Painel de Administrador
- 

## Requerimentos
- Django 2.2.7
- djangorestframework 3.10.3
- pkg-resources 0.0.0
- pytz 2019.3
- sqlparse 0.3.0
- Pillow 6.2.1

## Testando a minha API
#### Instalando a API
- Crie um novo ambiente virtual (env) e ative o mesmo
  - python3 -m venv nomeDoAmbiente
  - source nomeDoAmbiente/bin/activate

- Clone o meu projeto do github
  -  `git clone 'https://github.com/Pancitopenico/DjangoRestTutorial'`

- Instalando os requerimentos da API
  - pip install -r requirements.txt
  
- Instalando primeiros passos
  - python manage.py makemigrations
  - python manage.py migrate
  - python manage.py createsuperuser
  - python manage.py runserver
  
- Agora provavelmente tudo irá rodar perfeitamente.