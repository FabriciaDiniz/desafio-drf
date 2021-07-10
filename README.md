# desafio-drf

### Para rodar o programa pela primeira vez:
Certifique-se de que você tem o Python 3 instalado, clone o repositorio e:  
- instale as dependências usando `pip install -r requirements.txt`
- crie o banco de dados sqlite3 usando `python manage.py migrate`
- suba o servidor: `python manage.py runserver`
- o aplicativo roda em localhost:8000 e você pode acessar a página de admin em `/admin`

### Para rodar o programa das vezes seguintes
- suba o servidor: `python manage.py runserver`

### Para registrar um usuário/logar
- Registrar usuário comum: POST htttp://127.0.0.1:8000/users
  - passando como form data email, username, password e re_password
- Registrar superusuário: `python manage.py createsuperuser`
- Para logar e receber um token: POST http://127.0.0.1:8000/auth/token/login/
- Para fazer as demais operações, enviar um header Authorization com Token e o token recebido
- Para criar uma consulta: POST http://127.0.0.1/consultas/ passando o token no header e um json no body com agenda_id e horario 
- Para saber quais agendas estão disponíveis: GET http://127.0.0.1/agendas/
- Médicos e agenda são criados no painel de admin
