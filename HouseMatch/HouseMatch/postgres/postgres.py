from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
from HouseMatch.HouseMatch.models import House
import HouseMatch.HouseMatch.postgres.models as pm
import dataclasses
import HouseMatch.HouseMatch.config as cf

class Postgres:
    """
    Conncets and adds data to postgres 
    """
    def __init__(self):
        DATABASE_URL = "postgresql://postgres:postgres@localhost/HouseMatch"
        self.engine = create_engine(DATABASE_URL)    
        self.data_csv = pd.read_csv(f'{cf.HOME_PATH}/HouseMatch/HouseMatch/data_temp/cleaned_data.csv')
    
    def add_data_(self):
        self.data_csv.to_sql('house', self.engine, if_exists='append', index=False)
        

    def _get_attr_names(self):
        fields = dataclasses.fields(House)
        attribute_names = [field.name for field in fields]
        
        return attribute_names


if __name__ == "__main__":
    Postgres().add_data_()
