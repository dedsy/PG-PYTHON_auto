import pandas as pd

ya_df = pd.read_html('https://yandex.ru/pogoda/month?lat=53.90228271&lon=27.56183052&via=hnav')

print(ya_df)

data = ya_df[0]

for i in range(1, len(ya_df)):
    data = pd.concat([data,ya_df[i]], ignore_index=True)
