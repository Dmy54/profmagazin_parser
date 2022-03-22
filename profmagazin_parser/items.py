import scrapy


class ProfmagazinParserItem(scrapy.Item):
    category = scrapy.Field()
    price = scrapy.Field()
    med_wholesale = scrapy.Field()
    huge_wholesale = scrapy.Field()
    description = scrapy.Field()
    specification = scrapy.Field()
    image = scrapy.Field()
    name = scrapy.Field()
    article = scrapy.Field()
    href = scrapy.Field()
