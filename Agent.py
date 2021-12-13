import ipaddress
from colorama import Fore, Back, Style
import time
import os


class Agent():
    attribute = {
        "Server" : "",
        "ServerActive" : "",
        "Hostname" : "",
    }
    parameter = list()

    def __init__(self, dict, paras):
        self.attribute["Server"] = dict["Server"]
        self.attribute["ServerActive"] = dict["ServerActive"]
        self.attribute["Hostname"] = dict["Hostname"]
        self.parameter = paras

    def set_server(self, sv):
        try:
            if ipaddress.ip_address(sv):
                self.attribute["Server"] = sv
            else:
                time.sleep(1)
                print(Fore.RED + "[!] Invalid IP.")
                print(Style.RESET_ALL)
        except ValueError:
            time.sleep(1)
            print(Fore.RED + "[!] Invalid IP.")
            print(Style.RESET_ALL)
    
    

    def set_server_active(self, sa):
        try:
            if ipaddress.ip_address(sa):
                self.attribute["ServerActive"] = sa
            else:
                time.sleep(1)
                print(Fore.RED + "[!] Invalid IP.")
                print(Style.RESET_ALL)
        except ValueError:
            time.sleep(1)
            print(Fore.RED + "[!] Invalid IP.")
            print(Style.RESET_ALL)
    
    def set_hostname(self, hn):
        self.attribute["Hostname"] = hn

    

    def display_attribute(self):
        terminal_width = os.get_terminal_size().columns
        print(Fore.CYAN)
        print("-"*terminal_width)
        # Print the names of the columns.
        print ("{:<30} | \t {:<80}".format('Attribute', 'Value'))
        print("-"*terminal_width)
        # print each data item.
        for key, value in self.attribute.items():
            print("{:<30} | \t {:<80}".format(key, value))
            print("-"*terminal_width)
        print(Style.RESET_ALL)

    def add_parameter(self, item):
        self.parameter.append(item)

    def delete_parameter(self, idx_para):
        delete_para = self.parameter[idx_para]
        for idx, value in enumerate(self.parameter):
            if idx == idx_para:
                self.parameter.remove(delete_para)
            else:
                pass
        

    def update_parameter(self, changed_id, updated_item):
        for idx, value in enumerate(self.parameter):
            if idx == changed_id:
                self.parameter[idx] = updated_item
            else:
                pass

    def display_parameter(self):
        terminal_width = os.get_terminal_size().columns
        print(Fore.CYAN)
        #print("-"*terminal_width)
        # Print the names of the columns.
        print ("{:<10} |\t {:<80}".format('Index', 'User Parameters'))
        print("-"*terminal_width)
        for idx, value in enumerate(self.parameter):
            print("{:<10} |\t {:<80}".format(idx+1, value))
            print("-"*terminal_width)
        print(Style.RESET_ALL)
