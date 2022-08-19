import pandas as pd

#Getting the Data
idioms_data = pd.read_csv(r'Data\idioms_1.csv', sep=';')
print(idioms_data.iloc[10:50, 0:2])
