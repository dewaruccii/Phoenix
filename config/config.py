from genericpath import isdir, isfile
import os


def AppConfig():
    APP = {
        'APP_NAME': 'PhoeniX',
        'APP_VERSION': '1.0.0',
        'APP_AUTHOR': 'DewaRuccii',
        'APP_RUN': 'DEVELOPMENT',
        'APP_USER_API': 'admin',
        'APP_PASSWORD_API': 'Seratus45',
        'APP_AUTHOR_EMAIL': 'lioncompany48',
        'APP_AUTHOR_WEBSITE': 'https://rpl-21.my.id',
        'APP_BASE_WEBSITE': 'https://rpl-21.my.id',
        'APP_BASE_API': 'https://rpl-21.my.id/api/',
        'APP_BASE_DOWNLOAD': 'https://rpl-21.my.id/file/download/',
        'APP_BASE_PATH_CONFIG': 'C:/Users/{}/AppData/Local/PhoeniX/'.format(os.getlogin()),

    }
    return APP


# __MAIN__.py
