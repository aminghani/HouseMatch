import json

from itemadapter import ItemAdapter

class MyPipeline:
    def open_spider(self, spider):
        self.file = open("data_temp/items.jsonl", "a", encoding="utf-8")
    
    def close_spider(self, spider):
        self.file.close()


    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item