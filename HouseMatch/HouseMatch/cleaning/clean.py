import json
from HouseMatch.HouseMatch.models import House
import pandas as pd

TRANSLATION_TABLE = str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789")

class Clean:

    def __init__(self):
        self.data = self.load_raw_data()
        

    def load_raw_data(self):
        data = []
        with open('/home/amin/vscode/HouseMatch/HouseMatch/HouseMatch/data_temp/items.jsonl', 'r') as file:
            for line in file:
                data.append(json.loads(line))
        
        return data
    
    def clean(self):
        houses = []
        for record in self.data:
            title = record['title']
            price = record['price']
            if price is not None:
                try:
                    price = price.replace(',', "")
                    price = int(price)
                except:
                    price=None
            date = record['date']
            location_site = record['location_site']
            category_site = record['category_site']
            details = record['details']
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
            parking = None
            if 'پارکینگ' in details:
                parking = self._to_bool(details['پارکینگ'])
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
                    rent = details['رهن'].replace('تومان','')
                    rent = rent.replace(',', '')
                    mortgage = int(mortgage)
                except:
                    rent = None
            elevator = None
            if 'آسانسور' in details:
                elevator = self._to_bool(details['آسانسور'])
            warehouse = None
            if 'انباری' in details:
                warehouse = self._to_bool(details['انباری'])
            age = None
            if 'سن بنا' in details:
                age = details['سن بنا'].replace('سال', '')
                try:
                   age = int(age)
                except:
                    age = None 
            houses.append(House(title=title, price=price, date=date, location_site=location_site,
                                category_site=category_site, area=area, post_type=post_type, room_count=room_count,
                                parking=parking,mortgage=mortgage, rent=rent, elevator=elevator, warehouse=warehouse,
                                age=age))

        return houses

    def clean_and_save(self):
        houses = self.clean()
        data = [
            {"title": house.title, "price": house.price, "date": house.date, "location_site": house.location_site, 
             "category_site": house.category_site, "area": house.area, "post_type": house.post_type, 
             "room_count": house.room_count, "parking": house.parking, 
             "mortgage": house.mortgage, "rent": house.rent, "elevator": house.elevator, 
             "age": house.age,}
            for house in houses]
        df = pd.DataFrame(data)

        # Specify the CSV file path
        csv_file_path = "/home/amin/vscode/HouseMatch/HouseMatch/HouseMatch/data_temp/cleaned_data.csv"

        # Save the DataFrame to a CSV file
        df.to_csv(csv_file_path, index=False)

    def _to_bool(self, string):
        if string == 'دارد':
            return True
        else:
            False


    def print_data(self):
        print(self.data)

c = Clean()
c.clean_and_save()