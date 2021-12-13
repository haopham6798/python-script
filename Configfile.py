#!/usr/bin/python3
import os

class ConfigFile:
    lst_path = []
    rpath = str()


    def __init__(self, rpath):
        self.rpath = rpath


    def search_conf_file(self, name):
        print("ZMIS Config File: ")
        print("*"*50)
        #name="zabbix_agentd.conf"
        for root, dirs, files in os.walk(self.rpath):
            if name in files:
                self.lst_path.append(os.path.join(root, name))
        #self.get_user_input()
        return self.lst_path

    def display(self):
        for id, path in enumerate(self.lst_path):
            print(str(id+1) + path)
        