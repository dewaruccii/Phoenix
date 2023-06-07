import argparse
import configparser
import os
from tkinter import E
from cek.cek import CekValidToken
from comment.comment import *
from config.config import AppConfig
from colorama import Fore, Style, Back, init
from create.create import Create_Config_File
from get.get import getInfo, getInfoToken
from home.home import Home
from set.set import setDirectory
init(autoreset=True)

info = AppConfig()
config = configparser.ConfigParser()


def login():
    token = getInfo()
    token = token['AUTH']['token']
    if(CekValidToken(token)):
        Home().main()


def Auth(token):
    if(CekValidToken(token)):
        data = getInfoToken(token)
        print(Success("Token has been set"))
        return Create_Config_File(token, data['email'], data['id'])


parser = argparse.ArgumentParser(
    description='Welcome To PhoeniX', prog='{}'.format(info['APP_NAME']))
parser.add_argument('-a', '--auth', help='To insert Token to config')
parser.add_argument(
    '-d', '--dir', help='To set directory to save files default is current directory')
parser.add_argument(
    '-l', '--login', help='login on {}'.format(info['APP_NAME']), action='store_true')
parser.add_argument(
    '-v', '--version', help='Version of {}'.format(info['APP_NAME']), action='store_true')
args = vars(parser.parse_args())

if args['auth']:

    Auth(args['auth'])

if args['dir']:
    if(os.path.isdir(args['dir'])):
        setDirectory(args['dir'])
        print("Directory has been set to  "+Success(args['dir']))
        exit()
    else:
        print("Directory "+Error(args['dir']) +
              " is not exist, do you want to create it? [y/n] : ", end="")
        c = input()
        if c == 'y':
            os.mkdir(args['dir'])
            setDirectory(args['dir'])
            print("Directory has been created and set to " +
                  Success(args['dir']))
            exit()
        else:
            exit()
if(args['login']):
    login()
    # try:
    #     login()
    # except Exception as e:
    #     print(Error("Server Not Responding"))
    #     exit()
if(args['version']):
    version()


# cek config File
if os.path.isdir(info['APP_BASE_PATH_CONFIG']):
    if os.path.isfile(info['APP_BASE_PATH_CONFIG'] + "\config.ini"):
        pass
    else:
        Create_Config_File('', '', '')
else:
    os.mkdir(info['APP_BASE_PATH_CONFIG'])
    Create_Config_File('', '', '')
