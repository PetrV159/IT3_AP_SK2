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