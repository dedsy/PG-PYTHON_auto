import pandas
import collections
import openpyxl


def make_report(log_file_name: str, log_sheet_name: str,
                report_template_file_name: str, report_sheet_name: str,
                report_output_file_name: str):
    # Open Excel log journal
    excel_data = pandas.read_excel(log_file_name, sheet_name=log_sheet_name)

    # Open Excel report template
    wb = openpyxl.load_workbook(filename=report_template_file_name)
    sheet = wb[report_sheet_name]

    # Seven most common browsers
    browsers_count = collections.Counter(excel_data['Браузер'])
    browsers_most_common = browsers_count.most_common(7)

    # Get most common browsers and write cells
    sheet['A5'] = browsers_most_common[0][0]
    sheet['A6'] = browsers_most_common[1][0]
    sheet['A7'] = browsers_most_common[2][0]
    sheet['A8'] = browsers_most_common[3][0]
    sheet['A9'] = browsers_most_common[4][0]
    sheet['A10'] = browsers_most_common[5][0]
    sheet['A11'] = browsers_most_common[6][0]

    # Split products and define products variable
    products = []
    for product in excel_data['Купленные товары']:
        tmp = product.split(',')
        for el in tmp:
            products.append(el)

    # Seven most common products
    products_count = collections.Counter(products)
    products_most_common = products_count.most_common(7)

    # Get most common products and write cells
    sheet['A19'] = products_most_common[0][0]
    sheet['A20'] = products_most_common[1][0]
    sheet['A21'] = products_most_common[2][0]
    sheet['A22'] = products_most_common[3][0]
    sheet['A23'] = products_most_common[4][0]
    sheet['A24'] = products_most_common[5][0]
    sheet['A25'] = products_most_common[6][0]

    # Create dict, key = month number, value = visit count
    months = {}
    for i in range(1, 13):
        months.update({i: 0})

    # Count visitors by browser for each month
    # Create dict, key = popular browsers
    browser_by_month = {}
    for i in range(7):
        browser_by_month[browsers_most_common[i][0]] = months.copy()

    # Define variable for Date and Browser
    date_and_browsers = excel_data[['Дата посещения', 'Браузер']]

    # Define variable for Date and Products
    date_and_products = excel_data[['Дата посещения', 'Купленные товары']]

    # Count log rows
    rows = date_and_browsers.shape[0]

    # Columns in report file
    report_columns = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']

    # Extract month and browser and increase count in browser_by_month
    for i in range(rows):
        browser = date_and_browsers.loc[i]['Браузер']
        month = date_and_browsers.loc[i]['Дата посещения'].month
        if browser in browser_by_month.keys():
            browser_by_month[browser][month] += 1

    # Define list with most common browser names
    report_browsers = []
    for browser in browser_by_month.keys():
        report_browsers.append(browser)

    # Write count of visitors by month
    for row in range(7):
        for column in range(12):
            cell = str(report_columns[column]) + str(list(range(5, 12))[row])
            sheet[cell] = browser_by_month[report_browsers[row]][column + 1]

    # total of all visitors by month
    total = months.copy()
    for value in browser_by_month.values():
        for month, count in value.items():
            total[month] += count

    # Write total of all visitors by month
    column = 0
    for value in total.values():
        sheet[report_columns[column] + str(12)] = value
        column += 1

    # Create dict, key = popular products
    product_by_month = {}
    for i in range(7):
        product_by_month[products_most_common[i][0]] = months.copy()

    # Extract month and product and increase count in product_by_month
    for i in range(rows):
        product = date_and_products.loc[i]['Купленные товары']
        product = product.split(',')
        month = date_and_products.loc[i]['Дата посещения'].month
        for item in product:
            if item in product_by_month.keys():
                product_by_month[item][month] += 1

    # Create list with most common products
    report_products = []
    for item in product_by_month.keys():
        report_products.append(item)

    # Write count of products by month
    for row in range(7):
        for column in range(12):
            cell = str(report_columns[column]) + str(list(range(19, 26))[row])
            sheet[cell] = product_by_month[report_products[row]][column + 1]

    # total of all products by month
    total = months.copy()
    for value in product_by_month.values():
        for month, count in value.items():
            total[month] += count

    # Write total of all products by month
    column = 0
    for value in total.values():
        sheet[report_columns[column] + str(26)] = value
        column += 1

    # Populars and not populars products womens and mens
    sex_and_products = excel_data[['Пол', 'Купленные товары']]

    # Define lists of men and womens products
    men_products = []
    women_products = []

    # Extract month and product and increase count in product_by_month
    for i in range(rows):
        sex = sex_and_products.loc[i]['Пол']
        product = sex_and_products.loc[i]['Купленные товары']
        product = product.split(',')
        for item in product:
            if sex == 'м':
                men_products.append(item)
            else:
                women_products.append(item)

    # Counter men and women products
    men_products_counter = collections.Counter(men_products)
    women_products_counter = collections.Counter(women_products)

    # Most common product for men and women
    men_products_most_common = men_products_counter.most_common(1)[0][0]
    women_products_most_common = women_products_counter.most_common(1)[0][0]

    # Less common product for men and women
    result_men = men_products_counter.most_common()[:-(len(men_products_counter)+1):-1]
    result_women = women_products_counter.most_common()[:-(len(women_products_counter) + 1):-1]
    men_product_less_common = result_men[0][0]
    women_product_less_common = result_women[0][0]

    # Write cells with men and women data
    sheet['B31'] = men_products_most_common
    sheet['B32'] = women_products_most_common
    sheet['B33'] = men_product_less_common
    sheet['B34'] = women_product_less_common

    # Save report file
    wb.save(report_output_file_name)
