import scrapy


class HouseSale(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    date = scrapy.Field()
    location_site = scrapy.Field()
    category_site = scrapy.Field()
    details = scrapy.Field()

class Houserent(scrapy.Item):
    title = scrapy.Field()
    location = scrapy.Field()
    mortgage = scrapy.Field()
    rent = scrapy.Field()
    date = scrapy.Field()
    location_site = scrapy.Field()
    category_site = scrapy.Field()
    