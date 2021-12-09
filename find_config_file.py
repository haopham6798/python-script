#!/usr/bin/python3
import subprocess
import os
import time
import threading



def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

def get_user_input(lst):
    flag = False
    for id, val in enumerate(lst):
        print(str(id+1)+' - '+val)
    print("Which file you want to modify? ")
    try:
        user_input = int(input("Enter number to choose:"))
    except ValueError:
            print("Enter fucking number")
            

    while flag is False:
        if user_input < 0 or user_input > len(lst):
            print("Please enter valid number! ")
            user_input = input("Enter number to choose:")
        else:
            flag = True
            return user_input
        
        

def find_all(path):
    lst = []
    name="zabbix_agentd.conf"
    for root, dirs, files in os.walk(path):
        if "/usr" in root or "/etc" in root:   
            if name in files:
                lst.append(os.path.join(root, name))
    return lst
threads = []

def main():
    print("Start Searching . . .")
    """threadLock = threading.Lock()

    search_thread = threading.Thread(target=find_all, args=("/",threadLock))
    get_input_thread = threading.Thread(target=get_user_input, args=())
    
    search_thread.start()
    get_input_thread.start()

    search_thread.join()
    get_input_thread.join()"""

    lst = find_all("/")
    get_user_input(lst)

    print("Done")


main()