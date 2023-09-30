import pandas as pd
import re


# Читаем нашу страницу с погодой
ya_df = pd.read_html('https://yandex.ru/pogoda/month?lat=53.90228271&lon=27.56183052&lang=ru&via=hnav')

# DataFrame с которым мы будем работать
data = ya_df[0]

# Соединяем в удобный для работы список и сортируем его по числам
frames = [data['Пнпонедельник'],
          data['Втвторник'],
          data['Срсреда'],
          data['Чтчетверг'],
          data['Птпятница'],
          data['Сбсуббота'],
          data['Всвоскресенье']]
result = pd.concat(frames)

sorted_by_day = []
for i in range(0, 4):
    for x in result[i]:
        sorted_by_day.append(x)

# Создаём списки для данных будушего DataFrame
date = []
week_day = []
w_desc = []
day_temp = []
night_temp = []
pressure = []
humidity = []
wind_speed = []
fl = []

# Парсим список с данными упорядоченными по датам и записываем в заготовленные списки для каждой колонки
for i in sorted_by_day:
    pattern_number = r'^\d{1,2}'
    number = re.search(pattern_number, i.split(",")[0]).group(0)
    pattern_month = r'\w+$'
    month = re.search(pattern_month, i.split(",")[0]).group(0)
    date.append(number + " " + month)

    pattern_week_day = r'^\s\w+'
    week_day_str = re.search(pattern_week_day, i.split(",")[2]).group(0).strip().capitalize()
    week_day.append(week_day_str)

    pattern_w_desc = r'^.*'
    w_dec_str = re.search(pattern_w_desc, i.split(",")[4].split(';')[-1]).group(0).strip().capitalize()
    w_desc.append(w_dec_str)

    pattern_temp = r'^\s\d{1,2}'
    day_temp_str = re.search(pattern_temp, i.split(",")[3]).group(0).strip()
    day_temp.append(day_temp_str)
    night_temp_str = re.search(pattern_temp, i.split(",")[4]).group(0).strip()
    night_temp.append(night_temp_str)

    pattern_pressure = r'\d{3}\s\w{2}\s\w{2}.\s\w{2}.'
    pressure_str = re.search(pattern_pressure, i.split(",")[1]).group(0)
    pressure.append(pressure_str)

    pattern_humidity = r'\d{1,3}%'
    humidity_str = re.search(pattern_humidity, i.split(",")[1]).group(0)
    humidity.append(humidity_str)

    pattern_wind_speed = r'\d{1,2}\.\d{1}\s\w\/\w|\d{1,2}\s\w\/\w'
    wind_speed_str = re.search(pattern_wind_speed, i.split(",")[1]).group(0)
    wind_speed.append(wind_speed_str)

    pattern_fl = r'\d{4,5}'
    fl_str = re.search(pattern_fl, i.split(",")[1]).group(0)

    if len(fl_str) > 4:
        fl_str = fl_str[0:2]
    else:
        fl_str = fl_str[0]

    fl.append(fl_str)

# Создаем и заполняем DataFrame
result_df = pd.DataFrame(date, columns=['Date'])
result_df['Week day'] = week_day
result_df['Weather'] = w_desc
result_df['Day Temp'] = day_temp
result_df['Feels like'] = fl
result_df['Night Temp'] = night_temp
result_df['Pressure'] = pressure
result_df['Humidity'] = humidity
result_df['Wind speed'] = wind_speed

print(result_df)
