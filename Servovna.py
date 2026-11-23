import random
from datetime import datetime

class Server:
    def __init__(self, hostname:str, os:str, deployYear:int, warrantyYear:int, storageFree:int = 100):
        self.hostname = hostname
        self.os = os
        self.deployYear = deployYear
        self.warrantyYear = warrantyYear
        self.storageFree = storageFree
        pass

    def __str__(self):
        return f"{self.hostname} {self.os} {self.deployYear} - volné místo: {self.storageFree}%"
    

    def saveData(self):
        Data = (random.randint(5, 20))
        if self.storageFree >= Data:
            self.storageFree -= Data
            return f"Na server {self.hostname} se uložila data {Data}%. Zbýva {Data}% volného místa."
        else:
            return f"Chyba: Na serveru {self.hostname} není místo! Potřeba {Data}%, alek dispozici je jen {Data}%"
        
    
    def cleanDisk(self):
        clean = 100 - self.storageFree
        self.storageFree = 100
        return f"Disky na serveru {self.hostname} byly počištěny. Uvolnilo se {clean}% místa"
    
    def warrantyCheck(self):
        if self.warrantyCheck < datetime.now().year:
            return f"{self.hostname} {self.os} je po záruce v {self.warrantyYear}"
        else:
            return f"{self.hostname} {self.os} je pořádku o ukončení záruky zbývá do {self.warrantyYear- datetime.now().year}"
        
    

class serverRoom:
    def __init__(self, name:str):
        self.name = name
        self.servers = []
        pass

    def addServer(self, server:Server):
        self.servers.append(server)
        return f"{self.name} byl přidán do servovny: {server.hostname} {server.os}"
    
    def showServers(self):
        if len(self.name) == 0:
            print(f"Server v servovně {self.name} je prázdná")
        else:
            print(f"Server v servovně {self.name}")
            for server in self.servers:
                print("-->", server)

    
    def oldestServer(self):
        if len(self.servers) == 0:
            return None
        oldest = min(self.servers, key= lambda a: a.year)
        return oldest
    

    def avgStorage(self):
        if len(self.servers) == 0:
            return 0
        return sum(server.storage for server in self.servers) / len(self.servers)
    
