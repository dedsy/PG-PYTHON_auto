import json


def income_analyze(json_file: str):
    # Declare variables
    bands = {}
    styles = {}
    styles_results = {}
    monthly_fee = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}

    # Deserialize json
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

        for band in data['artists']:
            # Working with dict 'bands', k - artist name, v - dict with monthly fee
            if band['name'] not in bands.keys():
                bands[band['name']] = monthly_fee.copy()
            for month in bands[band['name']].keys():
                bands[band['name']][month] += band['monthly_calendar'][int(month) - 1] * band['fee'][int(month) - 1]

            # Working with dict 'styles', k - styles, v - dict with monthly fee
            if band['musical_style'] not in styles.keys():
                styles[band['musical_style']] = monthly_fee.copy()
            for month in styles[band['musical_style']].keys():
                styles[band['musical_style']][month] += band['monthly_calendar'][int(month) - 1] * band['fee'][int(month) - 1]

        # Working with dict styles_results with style names and year fee
        for k, v in styles.items():
            styles_results[k] = sum(v.values())

        # Search style with max year fee
        max_style = 0
        for k, v in styles_results.items():
            if v > max_style:
                max_style = v
                style = k

        # Search artist with min fee in this month
        # Sum of all styles
        min_band = sum(styles_results.values())
        for k, v in bands.items():
            if v[month] < min_band:
                min_band = v[month]
                band = k

        return style.capitalize() + " приносит музыкантам больше всего денег\n" + "В " + month + " месяце, на этом жанре можно заработать больше всего\n" + band + " меньше всего зарабатывает в этом месяце"


print(income_analyze("music.json"))
