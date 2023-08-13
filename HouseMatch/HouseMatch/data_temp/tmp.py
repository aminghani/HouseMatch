import pandas as pd

data = pd.read_csv('HouseMatch/HouseMatch/data_temp/cleaned_data.csv')

data = data.drop_duplicates()

print(data.shape[0])