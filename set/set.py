

from config.config import AppConfig
import configparser
info = AppConfig()


def setDirectory(cwd):
    config = configparser.ConfigParser()
    config.read(info['APP_BASE_PATH_CONFIG'] + 'config.ini')
    config.set('DIRECTORY', 'path', cwd)

    with open(info['APP_BASE_PATH_CONFIG'] + 'config.ini', 'w') as configfileObj:
        config.write(configfileObj)
