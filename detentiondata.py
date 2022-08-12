class DetentionForm:

    def __init__(self, name_surname, family_name, parents_names, mother_family_name, personal_num, address, job,
                 document):
        self.name_surname = name_surname
        self.family_name = family_name
        self.parents_names = parents_names
        self.mother_family_name = mother_family_name
        self.personal_num = personal_num
        self.address = address
        self.job = job
        self.document = document

        self.p_detain_dict_pos = {'name_surname_pos': [70, 87],
                                  'detention_time_pos': [380, 84],
                                  'detention_date_pos': [450, 84],
                                  'detention_place_pos': [70, 213],
                                  'officer_name_pos': [70, 238],
                                  'station_name_pos': [300, 238],
                                  'protocol_place_pos': [70, 273],
                                  'protocol_date_pos': [450, 273],
                                  'protocol_time_pos': [380, 273],
                                  'other_person_pos': [210, 300],
                                  'detention_person_pos': [115, 382],
                                  'family_name_pos': [375, 382],
                                  'parents_names_pos': [150, 407],
                                  'mother_family_name_pos': [375, 407],
                                  'personal_num_pos': [115, 446],
                                  'address_pos': [165, 520],
                                  'job_pos': [115, 546],
                                  'document_pos': [300, 572],
                                  }

    def collect_detention_data(self):
        detention_data = []

        # appending person data
        detention_data.append(self.name_surname)
        detention_data.append(self.family_name)
        detention_data.append(self.parents_names)
        detention_data.append(self.mother_family_name)
        detention_data.append(self.personal_num)
        detention_data.append(self.address)
        detention_data.append(self.job)
        detention_data.append(self.document)

        # appending detention data
        detention_date = input("Podaj datę zatrzymania\n")
        detention_data.append(detention_date)
        detention_time = input("Podaj godzinę zatrzymania\n")
        detention_data.append(detention_time)
        detention_base = input("Podaj podstawę prawną zatrzymania\n")
        detention_data.append(detention_base)
        detention_place = input("Podaj miejsce zatrzymania\n")
        detention_data.append(detention_place)
        officer_name = input("Podaj stopień, imie i nazwisko policjanta prowadzącego czynność\n")
        detention_data.append(officer_name)
        station_name = input("Podaj jednostkę Policji z której pochodzi funkcjonariusz\n")
        detention_data.append(station_name)
        protocol_place = input("Podaj miejsce sporządzania protokołu\n")
        detention_data.append(protocol_place)
        protocol_date = input("Podaj datę sporządzania protokołu\n")
        detention_data.append(protocol_date)
        protocol_time = input("Podaj godzinę sporządzania protokołu\n")
        detention_data.append(protocol_time)
        other_person = input("Inne osoby uczestniczące w czynności\n")
        detention_data.append(other_person)

        return detention_data

    # placing_person_data_to_detention_form_cells
    def place_data(self, person_data, p_detain_dict_pos, pdf):

        # iterating trough dictionary(p_detain_dict_pos) to set cells positions with input stored in "cells_info"
        # into "pdf" file
        for index, value in enumerate(p_detain_dict_pos.values()):
            pdf.set_xy(value[0], value[1])
            pdf.cell(50, 15, txt=f'{person_data[index]}', border=0)