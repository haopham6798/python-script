#!/usr/bin/python3
import os

class ConfigFile:
    def __init__(self, rpath):
        self.rpath = rpath
        self.lst_path = list()

    def search_conf_file(self, name):
        terminal_width = os.get_terminal_size().columns
        print("[+] ZMIS Config File: ")
        print("-"*terminal_width)

        #name="zabbix_agentd.conf"
        for root, dirs, files in os.walk(self.rpath):
            if name in files:
                self.lst_path.append(os.path.join(root, name))
        return self.lst_path

    def display(self):
        for id, path in enumerate(self.lst_path):
            print(str(id+1) + path)

            
        