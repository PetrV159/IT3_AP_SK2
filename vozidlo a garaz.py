import random

class Vozidlo:
    def __init__(self, znacka:str, rok_vyroby:int, stav_nadrze:int):
        self.znacka = znacka
        self.rok_vyroby = rok_vyroby
        self.stav_nadrze = stav_nadrze
        pass

    def zvuk_motoru(self):
        return "???"
    
    def info(self):
        return f"Vozidlo bylo vyrobeno od roku {self.rok_vyroby}"
    
    def startuj(self):
        return f"Dobře nastartuju to , no a štáva je {self.stav_nadrze}"




    
class Auto(Vozidlo):
    def __init__(self, znacka, rok_vyroby, stav_nadrze, typ_převodovky:str):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.typ_prevodovky = typ_převodovky


    def zvuk_motoru(self):
        return "Vrum, vrum!"   
    
    def zatrub(self):
        return "???"
    
auto = Auto("Škoda", 2016, 0, "čtyř ruční")

print(auto.typ_prevodovky)
print(auto.zvuk_motoru())
print(auto.info())
print(auto.startuj())
print(auto.zatrub())
print(" " * 20)

class Moped(Vozidlo):
    def __init__(self, znacka, rok_vyroby, stav_nadrze, ma_slapadla:bool):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.ma_slapadla = ma_slapadla

    def zvuk_motoru(self):
        return "Trrrrrrrrrr!"

    def slapej(self):
        if(random.randint(0,1) > 0):
            return f"no a {self.ma_slapadla} už nefunguje"
        else:
            return f"a {self.ma_slapadla} už funguje"

moped = Moped("Tatra", 1978, 200, "pedal")
print(moped.zvuk_motoru())
print(moped.info())
print(moped.startuj())
print(moped.slapej())
print(" " * 20)




garaz = [auto , moped]

for vozidel in garaz:
    print(vozidel.info())
    print(vozidel.zvuk_motoru())
    print(" " * 20)
