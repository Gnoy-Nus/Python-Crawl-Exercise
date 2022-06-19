import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy4.items import BookItem,ChapterItem

class CrawlspiSpider(CrawlSpider):
    name = 'CrawlSpi'
    # start_urls = ['https://pic.netbian.com/4kmeinv/index.html']
    # start_urls = ['https://www.bilibili.com/']
    start_urls = ['https://m.qidian.com/rank/yuepiao/']

    #链接提取器：根据正则进行提取
    # link = LinkExtractor(allow=r'index_\d+.html')
    # link = LinkExtractor(allow=r'https://www.bilibili.com/video/\.*?')
    link = LinkExtractor(allow=r'https://m.qidian.com/book/\d+.html')
    link_detail = LinkExtractor(allow=r'https://m.qidian.com/book/\d+/\d+.html')
    # 规则提取器:将链接提取器提取到的链接进行解析 ； follow为True时将链接提取器 继续作用到 提取的链接
    rules = (
        Rule(link, callback='parse_item', follow=True),
        Rule(link_detail,callback='parse_detail', follow=False)
    )
    # 小知识：Xpath中不能包含tbody，需改成//
    def parse_item(self, response):
        item = BookItem()
        item['book_url'] = response.url
        yield item

    def parse_detail(self, response):
        # print('detail:',response)
        item = ChapterItem()
        item['chapter_url'] = response.url
        yield item

