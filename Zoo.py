import random
from datetime import datetime

class Animal:
    def __init__(self, species:str, name:str, birthyear:int, checkupyear:int, energy:int = 100):
        self.species = species
        self.name = name
        self.birthyear = birthyear
        self.checkupyear = checkupyear
        self.energy = energy
        pass

    def __str__(self):
        return f"{self.species} {self.name} {self.birthyear} {self.energy}"
    
    def play(self):
        usage = (random.randint(5,20))
        if self.energy >= usage:
            self.energy -= usage
            return f"{self.species} {self.name} spotřeboval při hře {usage}% energie a zbývá mu {self.energy}%"
        else:
            f"{self.species} {self.name} je moc unavený. Potřebuje {usage}% energie, ale má jen {self.energy}%"

    def feed(self):
        filled = 100 - self.energy
        self.energy = 100
        return f"{self.species} {self.name} byl nakrmen a doplnil {filled}"
    
    def vetCheck(self):
        if self.checkupyear < datetime.now().year:
            return f"{self.species} {self.name} musí k veterináři - platnost prohlídky skončila v roce {self.checkupyear}"
        else:
            return f"{self.species} {self.name} má technickou v pořádku. Na technickou bude muset za následující počet let: {self.checkupyear- datetime.now().year}."
        

animal1 = Animal("Lev", "Alex", 2016, 2026, 85)
animal2 = Animal("Zebra", "Marty", 2018, 2022)
animal3 = Animal("Žirafa", "Melmen", 2014, 2028, 10)
animal4 = Animal("Levice", "Simba", 2020, 2024, 40)

print(animal1)
print(animal2)
print(animal3)
print(animal4)
print("-"*20)

print(animal1.play())
print(animal2.play())
print(animal3.play())
print(animal4.play())
print("-"*20)

print(animal1.feed())
print(animal2.feed())
print(animal3.feed())
print(animal4.feed())
print("-"*20)

class Zoo:
    def __init__(self, name:str):
        self.name = name
        self.animals = []
        pass
