import scrapy

class ProfmagazinSpiderList(scrapy.Spider):
    name = "profmagazin"
    allowed_domains = ["profmagazin.ru"]
    pages = 561

    def start_requests(self):
        default_url = "https://profmagazin.ru/allprods.php/?page="
        urls = [default_url+str(i) for i in range(1, self.pages+1)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


class ProfmagazinSpiderDetail(scrapy.Spider):
    name = "profmagazin_detail"
    allowed_domains = ["profmagazin.ru"]

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')