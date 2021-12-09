
class Agent():
    Server = ""
    ServerActive = ""
    Hostname = ""

    def __init__(self, dict):
        self.Server = dict["Server"]
        self.ServerActive = dict["ServerActive"]
        self.Hostname = dict["Hostname"]

    def set_server(self, server):
        self.server = server
    
    def set_server_active(self, sa):
        self.ServerActive = sa
    
    def set_hostname(self, hn):
        self.Hostname = hn


    def display(self):
        n = len(max(self.__dict__.values(), key=len)) + 80
        print("-"*n)
        # Print the names of the columns.
        print ("{:<20} | {:<80}".format('Attribute', 'Value'))
        print("-"*n)
        # print each data item.
        for key, value in self.__dict__.items():
            print("{:<20} | {:<80}".format(key, value))
            print("-"*n)

