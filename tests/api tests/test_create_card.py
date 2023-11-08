import requests, os
from dotenv import load_dotenv

def test_login():
    load_dotenv()
    response = requests.post(url='https://my.combo.cards/api/auth/login?fingerprint=1650830455',
                             data={'username': os.getenv('LOGIN'), 'password': os.getenv('PASSWORD')})
    auth_cookie = response.cookies.get('fastapiusersauth')
    print(response)
# залогиниться
# создать карту
# валидировать код ответа
#- [ ]  Значение в *response*.
# - [ ]  Cхема ответа