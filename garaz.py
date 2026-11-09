import random
from datetime import datetime

class Auto:
    def __init__(self, brand:str, model:str, rok:int, STKrok:int, palivo:int = 100):
        self.brand = brand
        self.model = model
        self.rok = rok
        self.STKrok = STKrok
        self.palivo = palivo
        pass

    def __str__(self): #metoda, která se volá jako základní pro vypis vlastností
        return f"{self.brand} {self.model} ({self.rok}) - palivo: {self.palivo} %"
    

    def pohyb(self):
        spotreba = random.randint(5,20)
        if self.palivo >= spotreba:
            #self.palivo = self.palivo - spotreba
            self.palivo -= spotreba
            return f"{self.brand} {self.model} spotřeboval {spotreba} % paliva a zbývá mu {self.palivo}."
        else:
            return f"{self.brand} {self.model} by do cíle nedojel. Potřebuje {spotreba} % paliva, ale má jen {self.palivo} % paliva."

    def doplneniPaliva(self):
        doplnil = 100 - self.palivo
        self.palivo = 100
        return f"{self.brand} {self.model} natankoval {doplnil} % paliva "

    def STK(self):
        if self.STKrok < datetime.now().year:
            return f"{self.brand} {self.model} musí na technickou - technická skončila v roce {self.STKrok}."
        else:
            return f"{self.brand} {self.model} má technickou v pořádku. Na technickou bude muset za následující počet let: {self.STKrok - datetime.now().year}."


auto1 = Auto("Škoda", "Octavia 3", 2016, 2026, 85)
auto2 = Auto("Volkswagen", "Golf 7", 2018, 2022, 10)
auto3 = Auto("Toyota", "Hilux", 2014, 2028, 3)


#testovací výpis
print(auto1)
print(auto2)
print(auto3)
print(" - "*20)

print(auto1.pohyb())
print(auto2.pohyb())
print(auto3.pohyb())
print(" - "*20)

print(auto2.doplneniPaliva())
print(auto3.doplneniPaliva())
print(" - "*20)

print(auto1.STK())
print(auto2.STK())
print(auto3.STK())
print(" - "*20)


class Garaz:
    def __init__(self, jmeno:str):
        self.jmeno = jmeno
        self.auta = []
        pass


    def pridatAuto(self, auto:Auto):
        self.auta.append(auto)
        return f"Do garáže {self.jmeno} bylo přidáno auto: {auto.brand} {auto.model}"
    

garaz = Garaz("Podzemní garáž")

print(garaz.pridatAuto(auto1))
print(garaz.pridatAuto(auto2))
print(garaz.pridatAuto(auto3))