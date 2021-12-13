from Agent import Agent
from Configfile import ConfigFile
from datetime import datetime
from colorama import Fore, Back, Style
import edit_zabbix_agent as attr_editor
import edit_parameter as para_editor
import time
import constant

def check_user_input(uinput):
    if not uinput:
        return False
    else:
        return True

def main():
    ExitFlag = False
    while ExitFlag is False:
        try:
            attr_editor.show_banner()
            name= input("Enter your filename (default: zabbix_agentd.conf): ")
            if check_user_input(name) is False:
                name = "zabbix_agentd.conf"
                
            config_path = ConfigFile("/")
            result_searching = config_path.search_conf_file(name)
            if constant.SYSTEM_NAME == "Linux":
                    conf_list = list(path for path in result_searching if "/usr" in path or "/etc" in path)
            else:
                conf_list = list(path for path in result_searching if "C:" in path or "D:" in path)

            if not result_searching:
                print(Fore.YELLOW + " File not found!")
                print(Style.RESET_ALL)
            else:
                conf_file_path = attr_editor.get_user_input(conf_list)
                if(conf_file_path):
                    try:
                        agent = Agent(attr_editor.extract_attr_from_file(conf_file_path), para_editor.extract_parameter_from_file(conf_file_path))
                        print("Current config of Zabbix Agent from {} \n".format(conf_file_path))
                        ExitFlag = attr_editor.menu(agent, conf_list, conf_file_path)
                        attr_editor.save_changed(agent.__dict__, conf_file_path)
                    except KeyError:
                        print(Fore.RED + "Your file is not zabbix config, try again")
                        print(Style.RESET_ALL)
                else:
                    break

        except PermissionError:
            time.sleep(2)
            print(Fore.YELLOW+"[!] You must run this script with administrator privilege - try again with sudo")
            print("[-] Your configuration is not saved!")
            print(Style.RESET_ALL)
            break

        except KeyboardInterrupt:
            print()
            break
main()
