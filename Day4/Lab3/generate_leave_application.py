import openpyxl
from docxtpl import DocxTemplate
import re

def generate_leave_application(excel_file: str, excel_sheet: str, doc_template: str):
    wb = openpyxl.load_workbook(filename=excel_file)
    sheet = wb[excel_sheet]

    doc = DocxTemplate(doc_template)

    row_count = sheet.max_row

    for i in list(range(2, row_count+1)):
        last_name = sheet['A' + str(i)].value
        name = sheet['B' + str(i)].value
        company = sheet['D' + str(i)].value
        vacation_start = sheet['F' + str(i)].value.strftime("%d.%m.%Y")
        vacation_end = sheet['G' + str(i)].value.strftime("%d.%m.%Y")
        email = sheet['E' + str(i)].value

        content = {'last_name': last_name,
                   'name': name,
                   'company': company,
                   'vacation_start': vacation_start,
                   'vacation_end': vacation_end}

        doc.render(content)
        doc.save(str(i)+'_'+last_name+'.docx')

        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        if not re.fullmatch(regex, email):
            print(f'Ошибка в email - {email} для {name} {last_name}')
