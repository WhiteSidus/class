class Car:

    """
    Cenu auta udavame v DPH
    """
    
    #je možnost kontroly vstupních dat ktere prijdou při instanci do objektu
    # Methoda
    def __init__(self, znacka: str,rok: int,model: str,barva: str,typ_prevodovky: str,cena: float): 
        self.znacka = str(znacka) #instance
        self.rok = int(rok)
        self.model = str(model)
        self.barva = str(barva)
        self.typ_prevodovky = str(typ_prevodovky)
        self.cena = float(cena)

    # Methoda
    def Vypis(self):
        return f"Nazev auta: {self.znacka}\nRok výroby: {self.rok}\nModel: {self.model}\nBarva: {self.barva}\nTyp prevodovky: {self.typ_prevodovky}\nCena včetně DPH: {self.cena} Kč\n"

    # Methoda
    def cena_bez_dph(self):
        return f"Nazev auta: {self.znacka} \nCena bez DPH: {(self.cena * 0.79)}"

""""
audi = Car("Audi",1999, "A4", "Stříbrna", "Manuální", 45000)
skoda = Car("Škoda", 2014, "Superb II", "Bíla", "Manuální", 310000)
"""

seznam_aut = [
    Car("Audi",1999, "A6", "Stříbrna", "Manuální", 50000),
    Car("Daewoo", 2004, "Lanos", "Šeda", "Manualní", 10000),
    Car("Škoda", 2014, "Superb II", "Bíla", "Manuální", 310000)
]

# print(audi.rok)
# print(skoda.model)
# print(audi.Vypis())
# print(skoda.cena_bez_dph())

# print("---------------")
# print(seznam_aut[0].znacka)
# print("---------------")

"""
for i in range (len(seznam_aut)):
    print(seznam_aut[i].Vypis())
    print("----------------")
"""

for auto in seznam_aut:
    print(auto.Vypis())
    print("----------------")