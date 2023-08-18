import scrapy
from bs4 import BeautifulSoup
from datetime import datetime
from items import HouseSale, Houserent
import HouseMatch.Metadata as md


class SheypoorSpider(scrapy.Spider):
    """
    This class extracts needed data from Sheypoor

    """
    name = "house_sheypoor"

    def __init__(self, *args, **kwargs):
        super(SheypoorSpider, self).__init__(*args, **kwargs)
        self.start_urls = md.build_urls_sheypoor()

    def parse(self, response):
        """
        Follows posts in the first page

        """
        url = response.url
        location_site = [loc for loc in md.LocationSheypoor if loc.value in url][0]
        category_site = [cat for cat in md.CategorySheypoor if cat.value in url][0]

        res = response.css('div.SMz-b')
        for el in res:
            link = el.css('a.qL9GS::attr(href)').get() 

            extra_args = {'location_site': location_site, 'category_site': category_site}
            yield response.follow(link, callback=self.parse_new_page, cb_kwargs=extra_args)



    def parse_new_page(self, response, location_site, category_site):
        """
        Extract the necessary fields
    
        """
        res = response.css('div.r2eAR').get()
        soup = BeautifulSoup(res, 'html.parser')
        title = soup.find('h1', {'class': 'mjNIv'})
        price = soup.find('strong', class_='')
        title_value = title.string if title else None
        price_value = price.string if price else None
        
        details = {}
        keys_detail = soup.find_all('p', {'class': "_2e124"})
        values_detail = soup.find_all('p', {'class': '_874-x'})

        for i in range(len(keys_detail)):
            details[keys_detail[i].string] = values_detail[i].string
        yield HouseSale(title=title_value, price=price_value, date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        
              location_site=location_site.value, category_site=category_site.value, details=details)

