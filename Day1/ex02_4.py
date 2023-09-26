import json


def csv2json(csv_file: str, json_file: str):
    data = []
    result = []
    with open(csv_file, encoding='utf-8') as file:
        file = file.readlines()
        for row in file:
            prep = row.split(",")
            prep[-1] = prep[-1].translate({ord('\n'): None})
            data.append(prep)

    for x in data[1:]:
        tmp = {}
        for el in x:
            tmp[data[0][x.index(el)]] = el
        result.append(tmp)

    json_string = json.dumps(result, indent=4)
    with open(json_file, 'w', encoding='utf-8') as file:
        file.write(json_string)

    print(json_string)


csv2json('output.csv', 'output.json')
