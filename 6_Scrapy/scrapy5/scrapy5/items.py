# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy5Item(scrapy.Item):
    img_name = scrapy.Field()
    img_src = scrapy.Field()
    img_data = scrapy.Field()
