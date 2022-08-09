import fpdf
from PyPDF2 import PdfFileWriter, PdfFileReader


# def collect_personal_data():
name_surname = input("Podaj Imie i Nazwisko\n")
# personal_num = input("Podaj PESEL\n")
# person_address = input("Podaj Miejsce zamieszkania (w formacie *Miasto, ul. xxxx*)\n")


# def collect_detention_data():
detention_date = input("Podaj datę zatrzymania\n")
detention_time = input("Podaj godzinę zatrzymania\n")
# detention_place = input("Podaj miejsce zatrzymania\n")
# detention_base = input("Podaj podstawę prawną zatrzymania\n")
# person_detention_place = input("Podaj miejsce zatrzymania osoby\n")
# officer_name = input("Podaj stopień, imie i nazwisko policjanta prowadzącego czynność\n")
# station_name = input("Podaj jednostkę Policji z której pochodzi funkcjonariusz\n")
# protocol_place = input("Podaj miejsce sporządzania protokołu\n")
# protocol_date = input("Podaj datę i godzinę sporządzania protokołu\n")


# collect_personal_data()
# collect_detention_data()


overlay_pdf_file_name = 'overlay_PDF.pdf'
pdf_template_file_name = 'p_detain.pdf'
result_pdf_file_name = 'final_PDF.pdf'

# This section creates a PDF containing the information you want to enter in the fields
# on your base PDF.
pdf = fpdf.FPDF(format='letter', unit='pt')
pdf.add_page()
pdf_style = ''

pdf.set_font("Arial", style=pdf_style, size=15)
pdf.set_xy(70, 87)
pdf.cell(150, 15, txt=name_surname, border=0, ln=0)

pdf.set_font("Courier", style=pdf_style, size=17)
pdf.set_xy(380, 84)
pdf.cell(50, 15, txt=detention_time, border=0, ln=0)
pdf.set_xy(450, 84)
pdf.cell(50, 15, txt=detention_date, border=0, ln=0)

pdf.output(overlay_pdf_file_name)
pdf.close()

p_detain_dict_pos = {'name_surname_pos': [70, 87],
                     'detention_time_pos': [380, 84],
                     'detention_date_pos': [450, 84],
                     'personal_num_pos': []}

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
