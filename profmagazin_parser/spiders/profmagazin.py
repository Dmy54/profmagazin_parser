import scrapy
from profmagazin_parser.items import ProfmagazinParserItem


class ProfmagazinSpider(scrapy.Spider):
    name = "profmagazin"
    allowed_domains = ["profmagazin.ru"]
    # выбираем количество страниц, которое парсить (на текущий момент 551)
    pages = 551

    def start_requests(self):
        default_url = "https://profmagazin.ru/allprods.php/?page="
        urls = [default_url+str(i) for i in range(1, self.pages+1)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_pages)

    def parse_pages(self, response, **kwargs):
        for url in response.css('.ci-title').xpath('@href').getall():
            url = "https://profmagazin.ru" + url
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        self.logger.info("Getting response %s", response.url)
        item = ProfmagazinParserItem()
        item['href'] = response.url
        item['name'] = response.xpath('//h1[@class="content-title"]/text()').get(default='not-found')
        item['category'] = ''.join(response.xpath('//ul[@class="breadcrumbs"]//text()').extract()).replace('\t', '')
        item['price'] = response.xpath('//div[@class="cb-price-text"]/meta[@itemprop="price"]/@content').get(default='not-found')
        item['med_wholesale'] = response.xpath('//div[@class="sub-prices"]/div[1]/text()').get(default='not-found')
        item['huge_wholesale'] = response.xpath('//div[@class="sub-prices"]/div[2]/text()').get(default='not-found')
        item['description'] = ''.join(response.xpath('//div[@class="card-desc-other-view"]//text()').extract()).replace('\r', '')
        item['specification'] = ';'.join(response.xpath('//div[contains(@class, "tab") and not(contains(@class, "active"))]/p//text()').extract())
        item['image'] = "https://profmagazin.ru" + response.xpath('//div[@class="card-desc-other-view"]/img/@src').get(default='not-found')
        item['article'] = response.xpath('//div[@class="cb-article"]/text()').get(default='not-found')
        return item
