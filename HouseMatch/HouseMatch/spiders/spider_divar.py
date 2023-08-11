import scrapy
from bs4 import BeautifulSoup
import HouseMatch.Metadata as md 
from items import HouseSale
from datetime import datetime

class DivarSpider(scrapy.Spider):
    name = "house_divar"
    
    def __init__(self, *args, **kwargs):
        super(DivarSpider, self).__init__(*args, **kwargs)
        self.start_urls = md.build_urls_divar()

    def parse(self, response):
        url = response.url
        location_site = [loc for loc in md.LocationDivar if loc.value in url][0]
        category_site = [cat for cat in md.CategoryDivar if cat.value in url][0]

        res = response.css('div.post-card-item-af972.kt-col-6-bee95.kt-col-xxl-4-e9d46')
        for el in res:
            link = el.css('a::attr(href)').get()
            title = el.css('h2.kt-post-card__title::text').get()
            price = el.css('div.kt-post-card__description::text').get()
            #price_value = price.srting if price else None
            #title_value = title.srting if title else None
            extra_args = {'location_site': location_site, 'category_site': category_site, 'title': title, 'price': price}
            yield response.follow(link, callback=self.parse_new_page, cb_kwargs=extra_args)
            

    def parse_new_page(self, response, location_site, category_site, title, price):
        res = response.css('div.post-page__section--padded').get()
        soup = BeautifulSoup(res, 'html.parser')
        details = {}
        detail_ = soup.find_all('div', {'class': "kt-base-row kt-base-row--large kt-unexpandable-row"})
        
        for detail in detail_:
            key = detail.find('p', {'class': "kt-base-row__title kt-unexpandable-row__title"})
            value = detail.find('p', {'class': "kt-unexpandable-row__value"}) or \
            detail.find('a', {'class': "kt-unexpandable-row__action kt-text-truncate"}) 
            details[key.string] = value.string
        attr = []
        attrs = soup.find_all('span', {'class': 'kt-group-row-item__value kt-body kt-body--stable'})
        elovator = attrs[0]
        parking = attrs[1]
        store = attrs[2]
        attr.append(elovator.string if elovator else None)
        attr.append(parking.string if parking else None)
        attr.append(store.string if store else None)
        details['attributes'] = attr
        yield HouseSale(title=title, price=price, location_site=location_site.value, category_site=category_site.value,
                         date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), details=details)