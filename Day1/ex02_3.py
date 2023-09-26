o_file = "output.csv"


def to_csv_file(filename: str, headers: list[str], rows: list[list[str]],
                delimeter: str = ",", new_line: str = "\n") -> None:
    with open(filename, 'w') as file:
        file.write(delimeter.join(headers) + new_line)
        file.writelines([delimeter.join(row) + new_line for row in rows])


headers_list = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']
data = [
    ['-122.050000', '37.370000', '27.000000', '3885.000000', '661.000000', '1537.000000', '606.000000', '6.608500', '344700.000000'],
    ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000', '176500.000000'],
    ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400', '270500.000000'],
    ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900', '330000.000000'],
]

to_csv_file(o_file, headers_list, data)

with open(o_file) as file:
    for line in file:
        print(line, end="")
