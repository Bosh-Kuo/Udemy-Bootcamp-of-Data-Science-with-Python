import pandas as pd

df = pd.read_html('https://en.wikipedia.org/wiki/Economy_of_the_United_States')[1]
df.to_csv('USA-indicators.csv', sep = ';', index = False)