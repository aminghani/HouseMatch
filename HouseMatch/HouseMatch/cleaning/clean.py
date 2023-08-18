import json
from HouseMatch.HouseMatch.models import House
import pandas as pd
import os
import HouseMatch.HouseMatch.config as cf

class Clean:
    """
    This class is used for cleaning the raw data
    and writing the result to a csv file
    """

    def __init__(self):
        self.data = self.load_raw_data()
        

    def load_raw_data(self):
        """
        load the raw data into a list and returns it

        Returns:
            list: return raw data in the list
        """
        data = []

        file_path = f'{cf.HOME_PATH}/HouseMatch/HouseMatch/data_temp/items.jsonl'

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                for line in file:
                    data.append(json.loads(line))
        
        return data
    
    def clean(self):
        """
        cleans the data and return the result in a list

        Returns:
            list: list of cleaned houses
        """
        houses = []

        for record in self.data:
            title = record['title']
            price = record['price']
            
            if price is not None:
                try:
                    price = price.replace(',', '')
                    price = price.replace('٬', '')
                    price = int(price)
                except:
                    price=None
            
            date = record['date']
            location_site = record['location_site']
            category_site = record['category_site']
            details = record['details']
            
            area = None
            if 'متراژ' in details:
                area = details['متراژ']
                area = area.replace(',', "")
                area = int(area)
            
            post_type = None
            if 'نوع ملک' in details:
                post_type = details['نوع ملک']
            
            room_count = None
            if 'تعداد اتاق' in details:
                if details['تعداد اتاق'] == 'بدون اتاق':
                    room_count = 0
                else:
                    try:
                        room_count = int(details['تعداد اتاق'])
                    except:
                        room_count = None
            
            mortgage = None
            if 'رهن' in details:
                try:
                    mortgage = details['رهن'].replace('تومان','')
                    mortgage = mortgage.replace(',', '')
                    mortgage = int(mortgage)
                except:
                    mortgage = None
            
            rent = None
            if 'اجاره' in details:
                try:
                    rent = details['اجاره'].replace('تومان','')
                    rent = rent.replace(',', '')
                    rent = int(rent)
                except:
                    rent = None
            
            if 'attributes' not in details:
                elevator = None
                if 'آسانسور' in details:
                    elevator = self._to_bool(details['آسانسور'])
            
                warehouse = None
                if 'انباری' in details:
                    warehouse = self._to_bool(details['انباری'])
            
                age = None
                parking = None
                if 'پارکینگ' in details:
                    parking = self._to_bool(details['پارکینگ'])
            
            age = None
            if 'سن بنا' in details:
                age = details['سن بنا'].replace('سال', '')
                try:
                   age = int(age)
                except:
                    age = None
            
            if 'ودیعه' in details and mortgage is None:
                try:
                    mortgage = details['ودیعه'].replace('تومان','')
                    mortgage = mortgage.replace('٬', '')
                    mortgage = int(mortgage)
                except:
                    rent = None
            
            if 'اجارهٔ ماهانه' in details and rent is None:
                try:
                    rent = details['رهن'].replace('تومان','')
                    rent = rent.replace('٬', '')
                    rent = int(rent)
                except:
                    rent = None
            
            if 'attributes' in details:
                attributes = details['attributes']
                if attributes[0] == 'آسانسور':
                    elevator = True
                else:
                     elevator = False
            
                if attributes[1] == 'پارکینگ':
                    parking = True
                else:
                     parking = False
            
                if attributes[2] == 'انباری':
                    warehouse = True
                else:
                     warehouse = False
            
            houses.append(House(title=title, price=price, date=date, location_site=location_site,
                                category_site=category_site, area=area, post_type=post_type, room_count=room_count,
                                parking=parking,mortgage=mortgage, rent=rent, elevator=elevator, warehouse=warehouse,
                                age=age))

        return houses

    def clean_and_save(self):
        """
        saves the clean data into a csv file
        """
        houses = self.clean()
        
        data = [
            {"title": house.title, "price": house.price, "date": house.date, "location_site": house.location_site, 
             "category_site": house.category_site, "area": house.area, "post_type": house.post_type, 
             "room_count": house.room_count, "parking": house.parking, 
             "mortgage": house.mortgage, "rent": house.rent, "elevator": house.elevator, 
             "age": house.age,}
            for house in houses]
        
        df = pd.DataFrame(data)
        df = df.drop_duplicates()
        
        csv_file_path = f"{cf.HOME_PATH}/HouseMatch/HouseMatch/data_temp/cleaned_data.csv"

        df.to_csv(csv_file_path, mode='a', header=False, index=False)

    def _to_bool(self, string):
        """
        util function for checking 

        Args:
            string (str): input string

        Returns:
            bool: true or false
        """
        if string == 'دارد':
            return True
        
        else:
            False

