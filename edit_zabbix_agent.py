import os
import re
import shutil
import fileinput
import platform as pfm
from agent import Agent

attributes = ['Server', 'ServerActive', 'Hostname']

def get_file_path():
    if(pfm.system() == 'Linux'):
        return './zabbix_agentd.conf' 
    else:
        return ''

def get_max_string(lst):
    return max(lst, key=len)

#chuyen cac gia tri thanh json
def convert_to_json(str, temp_dic):
    split_s = str.split('=')
    temp_dic[split_s[0]]=split_s[1]
    

#lay thong tin hien co trong file config cua zabbix_agentd.conf va luu vao dictionary
def get_config_attr(conf_file):
    sys_parameters = dict()
    with open(conf_file) as fr:
        lines = fr.readlines()
        for attr in attributes:
            for line in lines:
                if line.startswith(attr + '='):
                    convert_to_json(line.strip(), sys_parameters)
    fr.close()
    return sys_parameters

def set_config_attr(config_attributes, conf_file):
    current_config = []
    new_config_list = []
    modified_config_content = ""
    backup_file(conf_file)
    with open(conf_file, "r") as fout:
        lines = fout.readlines()
        for line in lines:
            current_config.append(line)
    


    for index, item in enumerate(current_config):
        for key, val in config_attributes.items():
            if item.startswith(key+'='):
                current_config[index] = (key+'='+val+'\n')
            else:
                continue

    fout.close()
    for r in current_config:
        modified_config_content += r

    with open(conf_file, 'w') as fin:
        fin.write(modified_config_content)
    
    fin.close()
    print("Replaced")


def display_infomation(d):
    n = len(get_max_string(d.values())) + 80
    print("-"*n)
    # Print the names of the columns.
    print ("{:<20} | {:<80}".format('Attribute', 'Value'))
    print("-"*n)
    # print each data item.
    for key, value in d.items():
        print("{:<20} | {:<80}".format(key, value))
        print("-"*n)



def menu(agent):
    flag = 1
    while(flag):
        agent.display()
        print('\n')
        print("Enter number to select options")
        
        print("1. Change Server\n")
        
        print("2. Change Server Active\n")
        
        print("3. Change Hostname\n")

        print("4. Exit\n")

        user_selection = input("Make your choice: ")
        
        if user_selection == "1":
            changed_data = input("Input your ip server: ")
            agent.set_server(changed_data)
        
        elif user_selection == "2":
            changed_data = input("Input your ip Server Active: ")
            agent.set_server_active(changed_data)
        
        elif user_selection == "3":
            changed_data = input("Input your ip Server Active: ")
            agent.set_hostname(changed_data)
        
        elif user_selection == "4":
            flag = 0
        else:
            print("I don't understand your choice.")

def backup_file(conf_file):
    source = conf_file
    destination = conf_file + '.bak'
    try:
        shutil.copyfile(source, destination)
        print("File copied successfully.")
 
    # If source and destination are same
    except shutil.SameFileError:
        print("Source and destination represents the same file.")
    
    # If destination is a directory.
    except IsADirectoryError:
        print("Destination is a directory.")
    
    # If there is any permission issue
    except PermissionError:
        print("Permission denied.")
    
    # For other errors
    except:
        print("Error occurred while copying file.")

def show_banner():
    print(""" 

          ____  _                       _   _                         
         |  _ \| |__   __ _ _ __ ___   | | | | ___   __ _ _ __   __ _ 
         | |_) | '_ \ / _` | '_ ` _ \  | |_| |/ _ \ / _` | '_ \ / _` |
         |  __/| | | | (_| | | | | | | |  _  | (_) | (_| | | | | (_| |
         |_|   |_| |_|\__,_|_| |_| |_| |_| |_|\___/ \__,_|_| |_|\__, |
                                                                |___/ 
                               _   _             
                              | | | | __ _  ___  
                              | |_| |/ _` |/ _ \ 
                              |  _  | (_| | (_) |
                              |_| |_|\__,_|\___/ 
    
      """)

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            #result.append(path+name)
            result.append(os.path.join(root, name))
    return result


def main():
    show_banner()
    conf_file_path = get_file_path()
    #config_attributes = get_config_attr(conf_file_path)
    agent = Agent(get_config_attr(conf_file_path))
    print("Current config of Zabbix Agent\n")
    menu(agent)
    agent.display()
    #set_config_attr(config_attributes, conf_file_path)
    set_config_attr(agent.__dict__, conf_file_path)

main()