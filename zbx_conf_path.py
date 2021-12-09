import os

class ZbxConfPath:
    zcpath = ""

    def search_file_cnf(path):
        result = []
        for root, dirs, files in os.walk(path):
            name="zabbix_agentd.conf"
            if name in files:
                #result.append(path+name)
                result.append(os.path.join(root, name))
        return result