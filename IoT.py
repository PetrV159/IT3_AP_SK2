import random

class ChytreZarizeni:
    def __init__(self, nazev:str, mistnost:str, zapnuto:bool):
        self.nazev = nazev
        self.mistnost = mistnost
        self.zapnuto = zapnuto
        pass

    def PrepniStav(self):
        if(random.randint(0,1) > 0):
            return "zapnuto"
        else:
            return "vypnuto"
    
    def provedAkci(self):
        return "Zařízení čeká na příkaz"
    



    
class ChytraZarovka(ChytreZarizeni):
    def __init__(self, nazev, misto, zapnuto, barva:str = "bílá"):
        super().__init__(nazev, misto, zapnuto)
        self.barva = barva


    def ProvedAkci(self):
        if(random.randint(0,1) > 0):
            return f" Je {self.PrepniStav} hnedka svítí {self.barva}"
        else:
            return f" Je {self.PrepniStav}"
    
    def ZmenBarvu(self, nNovaBarva:str):
        self.novabarva = nNovaBarva
        return f"Hned se přepnul na {nNovaBarva}"
    
zarovka = ChytraZarovka("???", "Obejvák", False)

print(zarovka.nazev)
print(zarovka.mistnost)
print(zarovka.ProvedAkci())
print(zarovka.ZmenBarvu("Červená"))
print(" " * 20)

class ChytraZasuvka(ChytreZarizeni):
    def __init__(self, nazev, misto, zapnuto, aktualni_odber_w:int):
        super().__init__(nazev, misto, zapnuto)
        self.aktualnivyberw = aktualni_odber_w

    def ProvedAkci(self):
        if self.aktualnivyberw:
            W = 1000
        else:
            W = "???"
        return f"Dnešní odběr je {self.aktualnivyberw} a Cena je {W}"

zasuvka = ChytraZasuvka("???", "ložnice", False, 200)
print(zasuvka.nazev)
print(zasuvka.mistnost)
print(zasuvka.ProvedAkci())
print(" " * 20)




