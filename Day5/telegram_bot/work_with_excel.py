import pandas
import collections
import openpyxl


def search_excel(search_string: str):
    excel_data = pandas.read_excel('people_data_vacation.xlsx', sheet_name='vacation')
    search_result = excel_data[excel_data.eq(search_string).any(axis=1)]

    result = []
    search_row_count = search_result.shape[0]

    for i in range(search_row_count):
        last_name = search_result.iloc[i]['Фамилия']
        name = search_result.iloc[i]['Имя']
        job_title = search_result.iloc[i]['Должность']
        company = search_result.iloc[i]['Компания']
        email = search_result.iloc[i]['Email']
        result.append(f'ФИО: {last_name} {name}\nДолжность: {job_title}\nКомпания: {company}\nEmail: {email}')

    return result
