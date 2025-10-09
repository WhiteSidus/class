# class - vlastnosti zaměstnanců (hoto)
# zamestnanci budou mít 3 metody
# 10 objektů, které budou v listu (hoto)
# pomocí loopu vypsat všechny zaměstnance (hoto)
# vypsat k nim jednu metodu
# Bonus - Základní vlastnost "ID" se generuje automaticky
 
class Zamestnanec:
    """Zadejte informace o zaměstnanci"""
    def __init__(self, Id: int, jmeno: str, prijmeni: str, vek: int, pracovni_pozice: str, plat: int):
        self.Id = int(Id)
        self.jmeno = str(jmeno)
        self.prijmeni = str(prijmeni)
        self.vek = int(vek)
        self.pracovni_pozice = str(pracovni_pozice)
        self.plat = int(plat)
 
    
    def vypis(self):
        """Vypíše všechny informace o zaměstnancích"""
        return f" Id: {self.Id}\n Jméno a příjmení: {self.jmeno} {self.prijmeni}\n Věk zaměstnance: {self.vek}\n Rok nástupu zaměstnance: {self.pracovni_pozice}\n Plat zaměstnance {self.plat} Kč\n {self.odměna()}"
    def odměna(self):
        """Přidá odměnu pro zaměstnance"""
        return f"Přidělená odměna zaměstnanci: {self.plat*0.10} Kč"
    def auto_id(self, Id: int):
        self.Id += 1
        return Id
 
 
seznam_zamestnancu = [
    Zamestnanec(1, "Pavel", "Nepil", 32, "uklízeč", 40000),
    Zamestnanec(2, "Jirka", "Ovčánek", 19, "uklízeč", 40000),
    Zamestnanec(3, "Marek", "Švýcar", 22, "pokladní", 45000),
    Zamestnanec(4, "Jirka", "Jiří", 45, "pokladní", 42500),
    Zamestnanec(5, "Jana", "Svobodová", 21, "pokladní", 45000),
    Zamestnanec(6, "Stanislav", "Tabulka", 50, "pokladní", 45000),
    Zamestnanec(7, "Roman", "Barkov", 38, "ostraha", 55000),
    Zamestnanec(8, "Zhorik", "Leshiyenko", 41, "skladní", 43000),
    Zamestnanec(9, "Karel", "Jelík", 18, "skladní", 43000),
    Zamestnanec(10, "Petra", "Jitra", 27, "skladní", 43000)
]
 
for zamestnanci in seznam_zamestnancu:
    print(zamestnanci.vypis())
    print("-" * 50)