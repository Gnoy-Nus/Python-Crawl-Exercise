# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy2Item(scrapy.Item):
    # define the fields for your item here like:
    img_name = scrapy.Field()
    img_src = scrapy.Field()
