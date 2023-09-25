import csv


def txt2csv(txt_file: str, csv_file: str, sep: str = ","):
    with open(txt_file, 'r') as input_file:
        stripped = (line.strip() for line in input_file)
        lines = (line.split(sep) for line in stripped if line)
        with open(csv_file, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(('name', 'count', 'price'))
            writer.writerows(lines)


txt2csv('prices.txt', 'prices.csv', '\t')
