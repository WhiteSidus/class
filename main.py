class Car:
    
    #je možnost kontroly vstupních dat ktere prijdou při instanci do objektu
    def __init__(self, znacka: str,rok: int,model: str,barva: str,typ_prevodovky: str,cena: float): 
        self.znacka = znacka
        self.rok = rok
        self.model = model
        self.barva = barva
        self.typ_revodovky = typ_prevodovky
        self.cena = cena

    def Vypis(self):
        return f"Nazev auta: {self.znacka}, Rok výroby: {self.rok}"

audi = Car("Audi",1999, "A4", "Stříbrna", "Manuální", 45000)
skoda = Car("Škoda", 2014, "Superb II", "Bíla", "Manuální", 310000)

print(audi.rok)
print(skoda.model)
print(audi.Vypis())