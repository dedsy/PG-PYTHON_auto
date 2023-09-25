import csv


def count_prices(csv_file: str):
    count = 0
    with open(csv_file, 'r') as input_file:
        reader = csv.reader(input_file)
        next(reader, None)
        for row in reader:
            count += int(row[1]) * int(row[2])
    return count


print(count_prices('prices.csv'))
