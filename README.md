# Blog simples em Django
- - - -
Este é um blog construido usando o Framework Django. **Este projeto ainda receberá atualizações.**

## Funcionalidades:
- Criação de novos posts
- Edição de posts já criados
- Exclusão de posts já criados
- Autenticação básica de usuários
- Sistema de Login e Registro de usuários
## Modificações para executar o projeto na sua máquina:
1. Abre seu terminal no diretório onde deseja clonar esse repositório e execute ```git clone https://github.com/Mathias206/Django-blog.git```
2. Crie um ambiente virtual
3. Instale Django e suas dependências
5. **IMPORTANTE!** Abra seu terminal e execute: ```python -c "import secrets; print(secrets.token_urlsafe())"```, copie a chave de valores gerada, vá em```config/settings.py```, apague o valor já definido em ```SECRET_KEY = ``` e cole a chave gerada em seu lugar. Para saber mais [clique aqui](https://docs.djangoproject.com/en/3.2/ref/settings/#secret-key)
6. Execute o comando ``` python manage.py makemigrations ```seguido por```python manage.py migrate ```
7. Execute o comando ```python manage.py createsuperuser```, saiba mais [aqui](https://docs.djangoproject.com/en/3.2/intro/tutorial02/#creating-an-admin-user)
8. Por fim, execute no seu terminal ```python manage.py runserver```, acesse pelo seu navegador http://127.0.0.1:8000/home e tudo deve estar funcionando. Em seguida vá em http://127.0.0.1:8000/admin e faça login com os dados criados no passo anterior.
