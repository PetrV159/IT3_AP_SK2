class NPC:
    def __init__(self, jmeno:str, energie:int):
        self.jmeno = jmeno
        self.energie = energie
        pass


    def predstavSe(self):
        return f"Zde NPC {self.jmeno}"
    
    def vyrazNa(self, cil:str):
        if self.energie >= 10:
            self.energie -= 10
            return f"{self.jmeno} se přesunul na {cil}. Zbývá energie: {self.energie}"
        else:
            return f"{self.jmeno} nemá dostatek energie pro přesun"


class Chodec(NPC):
    def __init__(self, jmeno, energie, domovska_ctvrt:str):
        super().__init__(jmeno, energie)
        self.domovska_ctvrt = domovska_ctvrt

    
    def predstavSe(self):
        return f"Zde je chodec {self.jmeno}, rajon: {self.domovska_ctvrt}"
    

    def vyrazNa(self, cil):
        if self.energie >= 30:
            self.energie -= 30
            return f"Zahajuji náročný pěší pochd k cíli {cil}. Zbývá energie: {self.energie}"
        else:
            return f"{self.jmeno} nemá dosatek energie"
        


class Policista(NPC):
    def __init__(self, jmeno, energie, zbran_tasena:bool):
        super().__init__(jmeno, energie)
        self.zbran_tasena = zbran_tasena

    
    def predstavSe(self):
        return f"Zde policista LSPD {self.jmeno}"
    
    def tasNeboSkryjZbran(self):
        self.zbran_tasena = not self.zbran_tasena
        if self.zbran_tasena:
            return f"{self.jmeno}: zbran tasena"
        else:
            return f"{self.jmeno}: zbran skryta v pouzdře"
        

class RidicAutobusu(NPC):
    def __init__(self, jmeno, energie):
        super().__init__(jmeno, energie)
        self.cestujici = []

    def naberCestijici(self, jmeno_cestujiciho):
        self.cestujici.append(jmeno_cestujiciho)
        return f"Do autobusu řidiče {self.jmeno} nastoupil cestujicí: {jmeno_cestujiciho}"

npc = NPC("CJ", 10)
print(npc.predstavSe())
print(npc. vyrazNa("strip"))
print(npc.vyrazNa("Grove Street"))
print(" - "*40)

npc1 = Chodec("Big Smoke", 40, "Grove Street")
print(npc1.predstavSe()) 
print(npc1.vyrazNa("čvrt Ballas"))
print(npc1.vyrazNa("gunshop"))
print(" - "*40)

npc2 = Policista("Frank Tenpenny" , 100)
print(npc2.predstavSe())
print(npc2.tasNeboSkryjZbran())
print(npc2.tasNeboSkryjZbran())
print(npc2.tasNeboSkryjZbran())
print(" - "*40)

npc3 = RidicAutobusu("Trevor", 20)
print(npc3.naberCestijici("Franklin"))
print(npc3.cestujici)
print(npc3.naberCestijici("Michael"))
print(npc3.cestujici)
print(" - "*40)

skupina_npc = [npc1, npc2, npc3]
spolecny_cil = "Vice City"

for postava in skupina_npc:
    print(postava.predstavSe())
    print(postava.vyrazNa(spolecny_cil))
    print("-"*40)