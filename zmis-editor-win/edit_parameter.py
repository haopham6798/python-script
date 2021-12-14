import time
import edit_zabbix_agent as attr_editor
import re

def change_parameter(agent):
    agent.display_parameter()
    changed_idx = int(input("> Enter index of parameter: "))
    changed_idx -= 1
    changed_para = input("> Enter your parameter: ")
    agent.update_parameter(changed_idx, changed_para)

def delete_parameter(agent):
    idx_para = int(input("> Enter index of parameter: "))
    idx_para -= 1
    agent.delete_parameter(idx_para)

def add_new_parameter(agent):
    new_para = input("> Enter your parameter: ")
    agent.add_parameter(new_para)

def edit_para_menu(agent, conf_list, conf_file_path):
    flag = 2
    print(conf_file_path)
    while flag >= 2:
        agent.display_parameter()
        print("1. Change user parameter\n")
        
        print("2. Delete user parameter\n")
        
        print("3. Add a new user parameter\n")

        print("4. Save & Exit\n")
        
        print("5. Back (Not Save)\n")

        print("> Enter number to select options")
        user_selection = input("> Make your choice: ")
        
        if user_selection == "1":
            change_parameter(agent)
        
        elif user_selection == "2":
           delete_parameter(agent)
        
        elif user_selection == "3":
            add_new_parameter(agent)
        
        elif user_selection == "4":
            #return True
            write_to_file(agent.parameter, conf_file_path)
            break

        elif user_selection == "5":
            attr_editor.menu(agent, conf_list, conf_file_path)

        else:
            time.sleep(2)
            print('-'*80)
            print("[-] I don't understand your choice.\n"+"Please Enter Again!")

    print()

def extract_parameter_from_file(conf_file):
    sys_parameters = list()
    with open(conf_file) as fr:
        lines = fr.readlines()
        for line in lines:
            if line.startswith("UserParameter="):
                value_para = re.sub(r'\AUserParameter=', r'', line)
                sys_parameters.append(value_para.replace("\n", ""))
    fr.close()
    return sys_parameters

def write_to_file(user_para, conf_file):
    with open(conf_file, 'a') as fin:
        for para in user_para:
            fin.write("UserParameter="+para+"\n")
    fin.close()
    print("[+] Your config is saved")

