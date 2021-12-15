import os
import re
import shutil
import fileinput
import platform
from Agent import Agent
from datetime import datetime
import time
import edit_parameter

def get_max_string(lst):
    return max(lst, key=len)

#chuyen cac gia tri thanh json
def convert_to_json(str, temp_dic):
    split_s = str.split('=')
    temp_dic[split_s[0]]=split_s[1]
    

#lay thong tin hien co trong file config cua zabbix_agentd.conf va luu vao dictionary
def extract_attr_from_file(conf_file):
    attributes = ["Server", "ServerActive", "Hostname"]
    sys_parameters = dict()
    with open(conf_file) as fr:
        lines = fr.readlines()
        for attr in attributes:
            for line in lines:
                if line.startswith(attr + '='):
                    convert_to_json(line.strip(), sys_parameters)
    fr.close()
    return sys_parameters

#ham backup va save cac thay doi
def save_changed(agent, conf_file):
    current_config = []
    modified_config_content = ""

    backup_file(conf_file)

    with open(conf_file, "r") as fout:
        lines = fout.readlines()
        for line in lines:
            if line.startswith("UserParameter="):
                pass
            else:
                current_config.append(line)
    
    for index, item in enumerate(current_config):
        for key, val in agent.attribute.items():
            if item.startswith(key+'='):
                current_config[index] = (key+'='+val+'\n')
            else:
                continue

    fout.close()
    for r in current_config:
        modified_config_content += r

    for para in agent.parameter:
        modified_config_content += "UserParameter="+para+"\n"

    with open(conf_file, 'w') as fin:
        fin.write(modified_config_content)
    
    fin.close()
    print("[+] Saved")


def menu(agent, conf_list, conf_file_path):

    flag = False

    while flag is False:

        agent.display_attribute()

        print("> Enter number to select options")
        
        print("1. Change Server\n")
        
        print("2. Change Server Active\n")
        
        print("3. Change Hostname\n")

        print("4. Edit UserParameter\n")
        
        print("5. Save & Exit\n")

        print("0. Back\n")

        user_selection = input("Make your choice: ")
        
        if user_selection == "1":
            changed_data = input("> Input your ip server: ")
            agent.set_server(changed_data)
        
        elif user_selection == "2":
            changed_data = input("> Input your ip Server Active: ")
            agent.set_server_active(changed_data)
        
        elif user_selection == "3":
            changed_data = input("> Input your ip Server Active: ")
            agent.set_hostname(changed_data)
        
        elif user_selection == "4":
            if edit_parameter.edit_para_menu(agent, conf_list, conf_file_path):
                break

        elif user_selection == "5":
            break
            
        elif user_selection == "0":
            get_user_input(conf_list)

        else:
            time.sleep(2)
            print('-'*80)
            print("I don't understand your choice."+ "Please Enter Again!")
    return True

def backup_file(conf_file_path):
    now = datetime.now()
    path_bak_folder = '/tmp/bak/'
    if(os.path.isdir(path_bak_folder)):
        pass 
    current_time = now.strftime("%H-%M-%S")
    source = conf_file_path
    destination = conf_file_path + '-' + current_time+ '.bak'
    try:
        shutil.copyfile(source, destination)
        print("[+] Backup file successfully.")
 
    # If source and destination are same
    except shutil.SameFileError:
        print("[-] Source and destination represents the same file.")
    
    # If destination is a directory.
    except IsADirectoryError:
        print("[-] Destination is a directory.")
    
    # If there is any permission issue
    except PermissionError:
        print("[!] Permission denied.")
    
    # For other errors
    except:
        time.sleep(1)
        print('[!] Error occurred while copying file.')
    


def show_banner():
    print(""" 

 _______  __ ___ ____        _____    _ _ _             
|__  /  \/  |_ _/ ___|      | ____|__| (_) |_ ___  _ __ 
  / /| |\/| || |\___ \ _____|  _| / _` | | __/ _ \| '__|
 / /_| |  | || | ___) |_____| |__| (_| | | || (_) | |   
/____|_|  |_|___|____/      |_____\__,_|_|\__\___/|_|   
    
    
      """)



def get_user_input(lst):
    flag = False
    user_input = int()
    for id, val in enumerate(lst):
        print(str(id+1)+' - '+val +"\n")


    print("Which file you want to modify? \n")
    
    while True:
        try:
            user_input = int(input("> Enter number to choose: "))
            return lst[user_input-1]
        except ValueError:
            time.sleep(2)
            print("[!] Your input is invalid, please enter again")
         
        except IndexError:
            time.sleep(2)
            print("[!] Please enter valid number! ")
        
    


