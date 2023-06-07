import configparser
import os
from config.config import AppConfig

info = AppConfig()


def Create_Config_File(token, email, id_user):

    config = configparser.ConfigParser()
    config['AUTH'] = {'token': token,
                      'email': email,
                      'id_user': id_user}

    config['DIRECTORY'] = {
        'path': os.getcwd()
    }
    with open(info['APP_BASE_PATH_CONFIG'] + 'config.ini', 'w') as configfile:
        config.write(configfile)


def CreaterDir(path):
    if not os.path.exists(path):
        os.makedirs(path)
