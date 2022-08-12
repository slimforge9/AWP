class PersonDataCreator:

    def __init__(self):
        self.person_data = []
        # def collect_personal_data():
        name_surname = input("Podaj Imie i Nazwisko\n")
        self.person_data.append(name_surname)
        family_name = input("Podaj Nazwisko Rodowe\n")
        self.person_data.append(family_name)
        parents_names = input("Podaj Imiona Rodziców\n")
        self.person_data.append(parents_names)
        mother_family_name = input("Podaj Nazwisko Panieńskie matki\n")
        self.person_data.append(mother_family_name)
        personal_num = input("Podaj PESEL\n")
        self.person_data.append(personal_num)
        address = input("Podaj adres zamieszkania\n")
        self.person_data.append(address)
        job = input("Praca/Zajęcie\n")
        self.person_data.append(job)
        document = input("podaj serie i numer dokumentu\n")
        self.person_data.append(document)
