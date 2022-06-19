# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    book_url = scrapy.Field()
class ChapterItem(scrapy.Item):
    chapter_url = scrapy.Field()