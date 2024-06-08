import scrapy
from scrapy.utils.url import url_query_parameter

class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["cian.ru"]
    start_urls = [
        'https://kazan.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=53&region=4777&room1=1'
    ]
    def parse(self, response):
        # выбираем область поиска на странице
        flats = response.css('div._93444fe79c--general--BCXJ4')
        page = url_query_parameter(response.url, 'p')  # номер страницы на которой находимся
        for flat in flats:
            heading_text = flat.css(
                'span[data-mark="OfferTitle"] span::text'
            ).get()  # заголовок каждого объявления
            # обработка ошибок на случай если объявление не стандартное
            try:
                yield {
                    'heading': heading_text,
                    'room': heading_text.split()[0],
                    'square': heading_text.split()[2],
                    'floor': heading_text.split()[4],
                    'address': flat.css('a[data-name="GeoLabel"]::text').getall(),
                    'price': flat.css('span[data-mark="MainPrice"] span::text').get(),
                    'id': str(flat.css('a._93444fe79c--link--VtWj6').attrib['href']).split('/')[-2],
                    'num_pages': page
                }
            except:
                yield {
                    'heading': heading_text,
                    'room': heading_text.split()[0],
                    'square': "",
                    'floor': "",
                    'address': flat.css('a[data-name="GeoLabel"]::text').getall(),
                    'price': flat.css('span[data-mark="MainPrice"] span::text').get().split(),
                    'id': str(flat.css('a._93444fe79c--link--VtWj6').attrib['href']).split('/')[-2],
                    'num_pages': page
                }
        show_button = response.xpath('//a[contains(text(),"Показать еще")]').get()
        next_page = response.xpath(
            '//nav[@class="_93444fe79c--pagination--VL341"]//a[@class="_93444'
            'fe79c--button--KVooB _93444fe79c--link-button--ujZuh _93444fe79'
            'c--M--I5Xj6 _93444fe79c--button--WChcG"]/span[contains('
            'text(),"Дальше")]/parent::a/@href'
        ).get()
        # обработка меню пагинации
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        else:
            if show_button is not None:
                yield response.follow(show_button, callback=self.parse)

# scrapy crawl myspider -O kirov.json
