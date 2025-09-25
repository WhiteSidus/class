class Car:

    """
    Cenu auta udavame v DPH
    """
    
    #je možnost kontroly vstupních dat ktere prijdou při instanci do objektu
    def __init__(self, znacka: str,rok: int,model: str,barva: str,typ_prevodovky: str,cena: float): 
        self.znacka = znacka
        self.rok = rok
        self.model = model
        self.barva = barva
        self.typ_prevodovky = typ_prevodovky
        self.cena = cena

    def Vypis(self):
        return f"Nazev auta: {self.znacka}\nRok výroby: {self.rok}\nModel: {self.model}\nBarva: {self.barva}\nTyp prevodovky: {self.typ_prevodovky}\nCena včetně DPH: {self.cena} Kč\n"

    def cena_bez_dph(self):
        return f"Nazev auta: {self.znacka} \nCena bez DPH: {(self.cena * 0.79)}"

audi = Car("Audi",1999, "A4", "Stříbrna", "Manuální", 45000)
skoda = Car("Škoda", 2014, "Superb II", "Bíla", "Manuální", 310000)

# print(audi.rok)
# print(skoda.model)
print(audi.Vypis())
print(skoda.cena_bez_dph())