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
8. Por fim, execute no seu terminal ```python manage.py runserver```, acesse pelo seu navegador http://127.0.0.1:8000/home e tudo deve estar funcionando. Em seguida vá em http://127.0.0.1:8000/admin e faça login com os dados criados no passo anterior para poder ter acesso a todas as funcionalidades do site.

![picture alt](https://lh3.googleusercontent.com/1pzqOT3uEhF-ok9ydOxpdXKRFtR6yYQll87OiaQO9zr0PkY59wvFyZfO8gfyTCEm5xObLpNiWG8UOgvKhInVbql1-_mOVGgdqnyaQ1rqP7tVtJJIq8hkj3gGVKNHfJGnLyOxIhhs-4ARmzU_UhEKNL9HoxXyxgk8kg13OPKpfLmb_YzOT-gBcn8wR3pbYRJGFDWcFXZU5UchV8aEPaqoSMFgdAvZkAA7W4NpGNFYdIqKFI69g6WZSASe7s6RScEpPOMrLpM0bzURF5YEW89R5RIjmAkhevdLKjlw8Zx2ys8PDNDeKr2gaNnsMq2C1gmUT1odOpi0DMRL5xLifhLxssCmLdfHeR-BVdPLbiTgUmz1c8MBylbpO3pdo0UTlHkVLvlrkp5RMI88w9xvGecAdCzUXntSumlGCKPRrBoPWSSePnM6pHzvY1jsM2aT_mWIR7iII_kRmpCFmIXnCnjXRYe4WtYRLpgU9r9rdvFetKkWhc7-e7Ln3RsTLcVaL4B6L9fTIXApCYTzRkIwJ7XwXWcf4BPZ1BIW1Wr6d2kAircTI2Me-O-5IlvjXVq5gaTvCZHb1QFvz3aNDrmHH1oBRBq83qTF6t8tO422yaRjThDs2Hkaf_h65-PVJ5qU3dcYj1DWsOwKLmivI7OjEmvdt3SQQ1hB5Ps9Lzyvp57796qvZbhABAKC9_fGxKd25OAXiAvIik2l66CcdMnOElZTsvzl=w1364-h671-no?authuser=0)
