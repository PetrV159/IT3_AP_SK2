class Hero:
    def __init__(self, jmeno:str, Lvl:int, Lokace:str = "Město"):
        self.jmeno = jmeno
        self.Lvl = Lvl
        self.lokace = Lokace
        pass

    def pokrik(self):
        return("???")
    
    def PredstavSe(self):
        return f"Jmenuji se {self.jmeno} mám uroveň {self.Lvl}"
    
    def KdeJsi(self):
        return f"Jsem v {self.lokace}"
    
    def PresunSe(self, nLokace:str):
        self.lokace = nLokace
        return f"Jsem teprve v {nLokace}"
    
hero = Hero("Vašek" , 30)
print(hero.pokrik())
print(hero.PredstavSe())
print(hero.KdeJsi())
print(hero.PresunSe("Brno"))
