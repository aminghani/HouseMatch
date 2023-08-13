import os

import pandas as pd

def delete_tmp_files():
    # Specify the file path
    
    file_path = '/home/amin/vscode/HouseMatch/HouseMatch/HouseMatch/data_temp/items.csv'

    if os.path.exists(file_path):
        # Remove the file
        os.remove(file_path)

def drop_duplicates():
    file_path = '/home/amin/vscode/HouseMatch/HouseMatch/HouseMatch/data_temp/cleaned_data.csv'
    data = pd.read_csv(file_path)
    data = data.drop_duplicates()
    data.to_csv(file_path, header=False, index=False)