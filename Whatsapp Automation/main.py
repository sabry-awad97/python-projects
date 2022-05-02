import os
import platform
from WhatsApp import WhatsApp
from Excel import ExcelReader
import art
from datetime import datetime

import time

from colorama import init, Fore

if __name__ == "__main__":
    init()

    # Clear the screen
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    # Display ASCII art
    print(art.text2art("Super"))
    print(Fore.CYAN + "\nCreated By:" + Fore.RESET + " Dr Sabry Awad\n")

    messenger = WhatsApp()
    es = ExcelReader()
    es.read()

    for entry in es.data:
        messenger.find_user(entry[es.phone_number_header])
        messenger.send_picture("./images/" + entry[es.image])
        if datetime.now().year == 2022:
            time.sleep(3)
