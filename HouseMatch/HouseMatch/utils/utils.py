import os
import HouseMatch.HouseMatch.config as cf
import pandas as pd

def delete_tmp_files():
    """
    delete the temp files
    """
    file_path = f'{cf.HOME_PATH}/HouseMatch/HouseMatch/data_temp/items.jsonl'

    if os.path.exists(file_path):
        
        os.remove(file_path)

def drop_duplicates():
    """
    drops the duplicates from csv file
    """
    file_path = f'{cf.HOME_PATH}/HouseMatch/HouseMatch/data_temp/cleaned_data.csv'

    data = pd.read_csv(file_path)
    data = data.drop_duplicates()

    data.to_csv(file_path, index=False)

def add_headers_csv():
    """
    gets csv without headers, adds header and write it back
    """
    file_path = f'{cf.HOME_PATH}/HouseMatch/HouseMatch/data_temp/cleaned_data.csv'

    if os.path.exists(file_path):
        headers = ["title", "price", "date", "location_site", 
                "category_site", "area", "post_type", 
                "room_count", "parking", 
                "mortgage", "rent", "elevator", 'warehouse',
                "age", ]
        
        df = pd.read_csv(file_path)
        df.columns = headers

        df.to_csv(file_path, index=False, header=True)




    