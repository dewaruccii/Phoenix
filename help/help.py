from config.config import AppConfig

info = AppConfig()


def main_help():
    print("""
    This is help menu

    command :
        auth : to insert token to config
        dir : to set directory to save files default is current directory
        logout : to logout from {}

    """.format(info['APP_NAME']))
