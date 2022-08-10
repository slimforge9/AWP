import fpdf
from PyPDF2 import PdfFileWriter, PdfFileReader

cell_addresses = []
# def collect_personal_data():
name_surname = input("Podaj Imie i Nazwisko\n")
cell_addresses.append(name_surname)
family_name = input("Podaj Nazwisko Rodowe\n")
cell_addresses.append(family_name)
parents_names = input("Podaj Imiona Rodziców\n")
cell_addresses.append(parents_names)
mother_family_name = input("Podaj Nazwisko Panieńskie matki\n")
cell_addresses.append(mother_family_name)
personal_num = input("Podaj PESEL\n")
cell_addresses.append(personal_num)
address = input("Podaj adres zamieszkania\n")
cell_addresses.append(address)
job = input("Praca/Zajęcie\n")
cell_addresses.append(job)
document = input("podaj serie i numer dokumentu\n")
cell_addresses.append(document)
#
#
# # def collect_detention_data():
detention_date = input("Podaj datę zatrzymania\n")
cell_addresses.append(detention_date)
detention_time = input("Podaj godzinę zatrzymania\n")
cell_addresses.append(detention_time)
detention_base = input("Podaj podstawę prawną zatrzymania\n")
cell_addresses.append(detention_base)
detention_place = input("Podaj miejsce zatrzymania\n")
cell_addresses.append(detention_place)
officer_name = input("Podaj stopień, imie i nazwisko policjanta prowadzącego czynność\n")
cell_addresses.append(officer_name)
station_name = input("Podaj jednostkę Policji z której pochodzi funkcjonariusz\n")
cell_addresses.append(station_name)
protocol_place = input("Podaj miejsce sporządzania protokołu\n")
cell_addresses.append(protocol_place)
protocol_date = input("Podaj datę sporządzania protokołu\n")
cell_addresses.append(protocol_date)
protocol_time = input("Podaj godzinę sporządzania protokołu\n")
cell_addresses.append(protocol_time)
other_person = input("Inne osoby uczestniczące w czynności\n")
cell_addresses.append(other_person)


# collect_personal_data()
# collect_detention_data()

# setting file names
overlay_pdf_file_name = 'overlay_PDF.pdf'
pdf_template_file_name = 'p_detain.pdf'
result_pdf_file_name = 'final_PDF.pdf'

# This section creates a PDF containing the information you want to enter in the fields
# on your base PDF.
pdf = fpdf.FPDF(format='letter', unit='pt')
pdf.add_page()
pdf_style = ''
pdf.add_font('DejaVu', fname='DejaVuSansCondensed.ttf')
pdf.set_font('DejaVu', size=11)

# creating dictionary of positions in pdf-forms
p_detain_dict_pos = {'name_surname_pos': [70, 87],
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
                     'address_pos':  [165, 520],
                     'job_pos': [115, 546],
                     'document_pos': [300, 572],
                     }

# iterating trough dictionary to set cells positions with input stored in memory
for index, value in enumerate(p_detain_dict_pos.values()):
    pdf.set_xy(value[0], value[1])
    pdf.cell(50, 15, txt=f'{cell_addresses[index]}', border=0)


pdf.output(overlay_pdf_file_name)
pdf.close()


# Take the PDF you created above and overlay it on your template PDF
# Open your template PDF
pdf_template = PdfFileReader(open(pdf_template_file_name, 'rb'))
# Get the first page from the template
template_page = pdf_template.getPage(0)
# Open your overlay PDF that was created earlier
overlay_pdf = PdfFileReader(open(overlay_pdf_file_name, 'rb'))
# Merge the overlay page onto the template page
template_page.mergePage(overlay_pdf.getPage(0))
# Write the result to a new PDF file
output_pdf = PdfFileWriter()
output_pdf.addPage(template_page)
output_pdf.write(open(result_pdf_file_name, "wb"))
