from elasticsearch import Elasticsearch
import pandas as pd
from HouseMatch.HouseMatch.models import House
import dataclasses
import json
import HouseMatch.HouseMatch.config as cf

class Elastic:
    def __init__(self):
        self.es = Elasticsearch(hosts=['https://localhost:9200'], http_auth=('elastic', cf.ELASTIC_PASS), 
                                verify_certs=False, timeout=30)
        self.cleaned_csv = pd.read_csv(f'{cf.HOME_PATH}/HouseMatch/HouseMatch/data_temp/cleaned_data.csv', 
                                       header=None)

    
    def add_data(self):
        attr_names = self._get_attr_names()
        num_rows = len(self.cleaned_csv)
        for i in range(num_rows):
            row_dic = {}
            row = self.cleaned_csv.iloc[i, :]
            for j in range(len(row)):
                row_dic[attr_names[j]] = str(row[j])
            json_object = json.JSONEncoder().encode(row_dic)
            self.es.index(index='houses', body=json_object)
        

    def _get_attr_names(self):
        fields = dataclasses.fields(House)
        attribute_names = [field.name for field in fields]
        return attribute_names

if __name__ == "__main__":
    Elastic().add_data()

