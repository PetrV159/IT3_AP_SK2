class Robot:
    def __init__(self, oznaceni:str, baterie:int, ukol:str = "Vař"):
        self.oznaceni = oznaceni
        self.baterie = baterie
        self.ukol = ukol
        pass

    def zvuk(self):
        return f"Ahoj!"
    
    def diagnostika(self):
        return f"Já jsem {self.oznaceni} a jedu na {self.baterie}!"
    
    def AktivniUkol(self):
        return f"Hnedka mám úkol {self.ukol}"
    
    def ZadejUkol(self, nUkol:str):
        self.ukol = nUkol
        return f"Samozřejmě! Aktivuju nový úkol {nUkol}"
    
robot = Robot("Pepa", 30)
print(robot.zvuk())
print(robot.diagnostika())
print(robot.AktivniUkol())
print(robot.ZadejUkol())
        