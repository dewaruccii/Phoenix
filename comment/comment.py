from colorama import Fore, Style, Back, init

from config.config import AppConfig
init(autoreset=True)

info = AppConfig()


def Logo():
    print(LightRed("""
        ██████╗ ██╗  ██╗ █████╗ ███████╗███╗  ██╗██╗██╗  ██╗
        ██╔══██╗██║  ██║██╔══██╗██╔════╝████╗ ██║██║╚██╗██╔╝
        ██████╔╝███████║██║  ██║█████╗  ██╔██╗██║██║ ╚███╔╝
        ██╔═══╝ ██╔══██║██║  ██║██╔══╝  ██║╚████║██║ ██╔██╗
        ██║     ██║  ██║╚█████╔╝███████╗██║ ╚███║██║██╔╝╚██╗
        ╚═╝     ╚═╝  ╚═╝ ╚════╝ ╚══════╝╚═╝  ╚══╝╚═╝╚═╝  ╚═╝
    """))


def version():
    print(Info(info['APP_NAME'] + " " +
          info['APP_VERSION'] + " " + info['APP_RUN']))


def Success(message):
    return Fore.GREEN + message + Style.RESET_ALL


def Error(message):
    return Fore.RED + message + Style.RESET_ALL


def Warning(message):
    return Fore.YELLOW + message + Style.RESET_ALL


def LightRed(message):
    return Fore.LIGHTRED_EX + message + Style.RESET_ALL


def Info(message):
    return Fore.CYAN + message + Style.RESET_ALL


def LightGreen(message):
    return Fore.LIGHTGREEN_EX + message + Style.RESET_ALL
