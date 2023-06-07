

import os
import requests
from requests.models import HTTPBasicAuth
from config.config import AppConfig
from colorama import Fore, Style, Back, init
import json
init(autoreset=True)
info = AppConfig()


def CekValidToken(token):

    data = {
        'api_key': token,
    }
    x = requests.get(info['APP_BASE_API'] + "users/", data,
                     auth=HTTPBasicAuth(info['APP_USER_API'], info['APP_PASSWORD_API']))
    json_data = json.loads(x.text)
    if(x.status_code == 200):
        return True
    elif(x.status_code == 400):
        print(Fore.RED + json_data['message'])
        return False
    else:
        print(Fore.RED + 'Token is invalid')
        return False


def cekFile():
    if(CekValidToken()):
        print("test")


def cekPath(path):
    if(os.path.exists(path)):
        return True
    else:
        return False
