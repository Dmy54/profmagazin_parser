import scrapy

class ProfmagazinParserListItem(scrapy.Item):
    url = scrapy.Field()


class ProfmagazinParserItem(scrapy.Item):
    categories = scrapy.Field()
    price = scrapy.Field()
    med_wholesale = scrapy.Field()
    huge_wholesale = scrapy.Field()
    description = scrapy.Field()
    specification = scrapy.Field()
    images = scrapy.Field()
    name = scrapy.Field()
    article = scrapy.Field()
