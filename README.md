# Django Rest Tutorial
Django Rest Tutorial entendendo o básico e criando uma API simpltes de pontos turísticos.

[Django Rest Framework Docs](https://www.django-rest-framework.org/).

## Pontos abordados na API

- Propor um novo ponto turistico - Qualquer pessoa.
- Moderação dos pontos turisticos cadastrados - Administradores da API.
- Listagem básica dos pontos turisticos (Lista resumida) - Via token.
- Listagem completa dos pontos turisticos - Via token.
- Detalhe de um ponto turistico - Via token.
- Atualização de um ponto turistico por usuários autorizados - Via token (Permissão especial)
- Deleção de um ponto turistico por usuários autorizados - Via token (Permissão especial)

## Endpoints da API
#### Estes são os primeiros endpoints da minha API
- http://127.0.0.1:8000/ => (GET) Contém a lista de todos os endpoints
- http://127.0.0.1:8000/api/pontos-turisticos/ => (GET) Listagem de todos os pontos turisticos
- http://127.0.0.1:8000/api/pontos-turisticos/ => (POST) Adiciona um novo ponto turistico
- http://127.0.0.1:8000/api/pontos-turisticos/1/ => (GET) Mostra um ponto turistico apenas, sendo o numero 1 o id do objeto
- http://127.0.0.1:8000/api/pontos-turisticos/1/ => (PUT) Atualiza as informações do meu ponto turistico, sendo o numero 1 o id do objeto
- http://127.0.0.1:8000/api/pontos-turisticos/1/ => (DELETE) Deleta um ponto turistico apenas, sendo o numero 1 o id do objeto
- Segue o mesmo padrão para os demais endpoints.
- http://127.0.0.1:8000/api/atracoes/
- http://127.0.0.1:8000/api/enderecos/
- http://127.0.0.1:8000/api/comentarios/
- http://127.0.0.1:8000/api/avaliacoes/

#### Endpoints especiais
Este endpoint foi criado para que eu consiga fazer a "Moderação dos pontos turisticos cadastrados".
- http://127.0.0.1:8000/api/pontos-turisticos-aprovados => (GET) Retorna todos os pontos turisticos aprovados

## Alterações do Administrador
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