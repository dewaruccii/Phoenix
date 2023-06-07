

def commandList():
    c = {
        'help': 'main_help()',
        'exit': 'self.exitB()',
        'version': 'version()',
        'file': 'table(getFile())',
        'dd': 'dd()',
        'cdd': 'cdd(com[0:])',
        'ls': 'ls()',
        'clear': 'clear()',
        'download': 'download(com[0:])',
        'camera': 'camera()',
    }
    return c
