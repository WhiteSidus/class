class person:
    def __init__(self, id: int, name: str, surname: str, age: int, gender: str):
        self.id = int(id)
        self.name = str(name)
        self.surname = str(surname)
        self.age = int(age)
        self.gender = str(gender)

# student a zamestnanec bude mít společné vlastnosti
# student a zamestnanec budou mít 3 vlastní vlastnosti navíc


# Dědičnost
class student(person):
    
    def __init__(self, id: int, name: str, surname: str, age: int, gender: str, year: int, faculty: str):
        super().__init__(id, name, surname, age, gender)
        self.year = int(year)
        self.faculty = str(faculty)


class zamestnanec(person):

    def __init__(self, name: str, surname: str, age: int, gender: str, position: str, subject: str, salary: float):
        super().__init__(name, surname, age, gender)
        self.position = str(position)
        self.subject = str(subject)
        self.salary = float(salary)

    def vypis(self):
        return f"ID: {self.id}\nJméno: {self.name}\nPříjmení: {self.surname}\nVěk: {self.age}\nPohlaví: {self.gender}\nPozice: {self.position}\nPředmět: {self.subject}\nPlat: {self.salary} Kč\n"
    

seznam_zamestnancu = [
    zamestnanec("Jan", "Novak", 30, "M", "Učitel", "Matematika", 50000),
    zamestnanec("Petr", "Svoboda", 40, "M", "Učitel", "Fyzika", 55000),
    zamestnanec("Eva", "Novotna", 35, "F", "Učitel", "Chemie", 52000)
]

for i in seznam_zamestnancu:
    print(i.vypis())
    print("---------------")