import os
# Import pandas
import pandas as pd

path = './INDICADORES/xlsx'
 
frames = []
files = os.listdir(path)
for filename in files:
    print(filename)
    data = pd.ExcelFile(path + '/' + filename)
    df = data.parse(0)
    frames.append(df)

# https://pandas.pydata.org/pandas-docs/stable/merging.html
result = pd.concat(frames)

# print(result)
result.to_csv('result.csv', sep=';', encoding='utf-8')