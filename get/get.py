
import configparser
import json

import requests
from requests.models import HTTPBasicAuth
from cek.cek import CekValidToken
from config.config import AppConfig

info = AppConfig()


def getInfo():
    config = configparser.ConfigParser()
    config.read(info['APP_BASE_PATH_CONFIG'] + 'config.ini')
    return config


def getInfoToken(token):
    if(CekValidToken(token)):
        data = {
            'api_key': token,
        }
        x = requests.get(info['APP_BASE_API'] + "users/", data,
                         auth=HTTPBasicAuth(info['APP_USER_API'], info['APP_PASSWORD_API']))
        json_data = json.loads(x.text)
        return json_data


def getFile():
    token = getInfo()
    token = token['AUTH']['token']
    if(CekValidToken(token)):
        data = {
            'api_key': token,
            'author': getInfo()['AUTH']['email']
        }
        x = requests.get(info['APP_BASE_API'] + "files/", data,
                         auth=HTTPBasicAuth(info['APP_USER_API'], info['APP_PASSWORD_API']))
        json_data = json.loads(x.text)
        return json_data
    else:
        return exit()


def getOneFile(id_file):
    listFile = getFile()
    data = {}
    for i in listFile:
        data = i
        if data['id_file'] == id_file:
            break
        else:
            data = {}
            continue
    return data
