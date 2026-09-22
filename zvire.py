import random

class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto
        pass

    def zvuk(self):
        return "???"

    def predstavSe (self):
        return f"Jmenuji se {self.jmeno} a je mi {self.vek}"
    
    def KdeJsi (self):
        return f"Jsem v místě zvaném {self.misto}"
    
    def JdiNa(self, nMisto:str):
        self.misto = nMisto
        return f"Šel jsem na {nMisto}"
    

class Had(Zvire):
    def __init__(self, jmeno, vek, delkaCm:int, jedovatý:bool, misto = "poušť"):
        super().__init__(jmeno, vek, misto)
        self.delkaCm = delkaCm
        self.jedovatý = jedovatý
    
    def zvuk(self):
        return "Ssssss"
    
    def predstavSe(self):
        if self.jedovatý:
            typ = "jedovatý"
        else:
            typ = "škrtič"
        return f"Ssssss... já jsem {self.jmeno}, měřím {self.delkaCm} a já jsem {typ}"
    

betka = Had("Betka", 8, 250, False)
print(betka.predstavSe())

    

class Kocka(Zvire):
    def __init__(self, jmeno, vek, barva, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.barva = barva
    
    def zvuk(self):
        return "Meow"
    
    def utok(self):
        return f"Kočka {self.jmeno} tě navštvaně poškrábala"
    
    def pohladit(self):
        if(random.randint(0,1) > 0):
            return self.utok()
        else:
            return f"{self.jmeno} se nechala pohladit a spokojeně přede!"


mourek = Kocka("Mourek", 4, "černý", "Kavárna")

print(mourek.jmeno)
print(mourek.barva)
print(mourek.KdeJsi())
print(mourek.zvuk())
print(mourek.utok())
print(mourek.pohladit())
print(mourek.predstavSe())
print(mourek.JdiNa("Parapet okna."))
print(" " * 20)

class Pes(Zvire):
    def __init__(self, jmeno, vek, plemeno, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.plemeno = plemeno

    def zvuk(self):
        return "Haf, haf!"

    def aport(self):
        return f"{self.jmeno} přinesl jsi míček"

    def vycesat(self):
        if(random.randint(0,1) > 0):
            return f"{self.jmeno} utekl před tvým kartáčem"
        else:
            return f"{self.jmeno} se nechal vyčesat"
        
    def predstavSe(self):
        return f"{super().predstavSe()} jsem {self.plemeno}"

radegast = Pes("Radegast", 5, "Australský ovčák", "gauč")

print(radegast.jmeno)
print(radegast.plemeno)
print(radegast.KdeJsi())
print(radegast.aport())
print(radegast.vycesat())
print(radegast.predstavSe())
print(" " * 20)


zvire = Zvire("Pepa", 42,)
print(zvire.jmeno)
print(zvire.vek)
print(zvire.misto)
print(zvire.zvuk())
print(zvire.predstavSe())
print(zvire.KdeJsi())
print(zvire.JdiNa("Kadeřnictví"))
print(zvire.KdeJsi())


zvire2 = Zvire("Jan", 32, "PentHouse")
print(zvire2.jmeno)
print(zvire2.predstavSe())
print(zvire2.KdeJsi())
print(zvire2.JdiNa("Klokánek"))
print(zvire.KdeJsi())

zoo = [radegast, mourek, betka]

for obyvatel in zoo:
    print(obyvatel.prestavSe())
    print(obyvatel.zvuk())
    print(" " * 20)
