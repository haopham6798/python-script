#!/usr/bin/python3
import os
from colorama import Fore, Back, Style

from colorama.ansi import Fore

class ConfigFile:
    lst_path = []
    rpath = str()


    def __init__(self, rpath):
        self.rpath = rpath


    def search_conf_file(self, name):
        terminal_width = os.get_terminal_size().columns
        print(Fore.GREEN + "[+] ZMIS Config File: ")
        print("-"*terminal_width)
        print(Style.RESET_ALL)
        #name="zabbix_agentd.conf"
        for root, dirs, files in os.walk(self.rpath):
            if name in files:
                self.lst_path.append(os.path.join(root, name))
        return self.lst_path

    def display(self):
        for id, path in enumerate(self.lst_path):
            print(Fore.GREEN + str(id+1) + path)
        print(Style.RESET_ALL)
            
        