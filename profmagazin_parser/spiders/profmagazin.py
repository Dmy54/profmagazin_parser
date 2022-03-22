import scrapy
from profmagazin_parser.items import ProfmagazinParserItem


class ProfmagazinSpider(scrapy.Spider):
    name = "profmagazin"
    allowed_domains = ["profmagazin.ru"]
    pages = 5

    def start_requests(self):
        default_url = "https://profmagazin.ru/allprods.php/?page="
        urls = [default_url+str(i) for i in range(1, self.pages+1)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_pages)

    def parse_pages(self, response, **kwargs):
        for url in response.css('.ci-title').xpath('@href').getall():
            url = "https://profmagazin.ru/" + url
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        self.logger.info("Getting response %s", response.url)
        item = ProfmagazinParserItem()
        item['name'] = response.xpath('').get()
        item['category'] = response.xpath('').get()
        item['price'] = response.xpath('').get()
        item['med_wholesale'] = response.xpath('').get()
        item['huge_wholesale'] = response.xpath('').get()
        item['description'] = response.xpath('').get()
        item['specification'] = response.xpath('').get()
        item['images'] = response.xpath('').get()
        item['article'] = response.xpath('').get()
        return item
