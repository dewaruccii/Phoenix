import sys
import os
from commandList.commandList import commandList
from comment.comment import *
from config.config import AppConfig
from get.get import getFile, getInfo
from help.help import main_help
from table.table import table
from command.command import *
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


class Home:
    def __init__(self):
        self.ginfo = getInfo()
        self.logo = 0

    def exitB(self):
        print("Bye")
        return exit()

    def main(self):
        if(self.logo == 0):
            Logo()
            self.logo += 1
        com = input(self.ginfo.get('AUTH', 'email') + '> ')
        com = com.split(" ")
        cm = com[0]
        com.pop(0)

        c = commandList()

        if(c.get(cm)):
            exec(c.get(cm))
            return self.main()
        else:
            print(Error("Command not found"))
            return self.main()
        # if(lencm > 0):
        #     if(c.get(cm)):
        #         exec(c.get(cm))
        #         return self.main()
        #     else:
        #         print(Error("Command not found"))
        #         return self.main()
        # else:
        #     if(c.get(cm)):
        #         exec(c.get(cm))
        #         return self.main()
        #     else:
        #         print(Error("Command not found"))
        #         return self.main()
