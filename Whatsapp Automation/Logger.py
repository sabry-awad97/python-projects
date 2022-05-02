from datetime import datetime
from termcolor import colored


class Logger:

    @staticmethod
    def log(message, level):
        if level == 'INFO':
            print('[' + colored(datetime.now().strftime('%H:%M:%S'),
                                'cyan') + '][' + colored('INFO', 'green') + '] ' + message)
        elif level == 'WARNING':
            print('[' + colored(datetime.now().strftime('%H:%M:%S'),
                                'cyan') + '][' + colored('WARNING', 'yellow') + '] ' + message)
        elif level == 'ERROR':
            print('[' + colored(datetime.now().strftime('%H:%M:%S'),
                                'cyan') + '][' + colored('ERROR', 'red') + '] ' + message)
