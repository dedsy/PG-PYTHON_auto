import openpyxl
from docxtpl import DocxTemplate
import re
from docx import Document


def generate_leave_application(excel_file: str, excel_sheet: str, doc_template: str, email_errors_file: str):
    wb = openpyxl.load_workbook(filename=excel_file)
    sheet = wb[excel_sheet]

    doc = DocxTemplate(doc_template)

    email_doc = Document()
    table = email_doc.add_table(rows=1, cols=2, style='Table Grid')
    table.cell(0, 0).paragraphs[0].add_run('ФИО').bold = True
    table.cell(0, 1).paragraphs[0].add_run('email').bold = True

    row_count = sheet.max_row

    wrong_emails = {}

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

        full_name = str(last_name + " " + name)

        if not re.fullmatch(regex, email):
            d = {full_name: email}
            wrong_emails.update(d)

    if len(wrong_emails) > 0:
        for k, v in wrong_emails.items():
            row = table.add_row()
            row.cells[0].text = k
            row.cells[1].text = v

    email_doc.save(email_errors_file)
