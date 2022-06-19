import scrapy
from selenium import webdriver
from selenium.webdriver.edge.options import Options
class MiddleSpider(scrapy.Spider):
    name = 'middle'
    start_urls = ['https://pic.netbian.com/4kmeinv/index.html']
    target_urls =[]
    def __init__(self):
        edge_options = Options()
        edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 规避检测
        self.bro =webdriver.Edge(executable_path='C:/Users/sun/Desktop/爬虫/6_Scrapy/scrapy3/scrapy3/spiders/msedgedriver.exe', options=edge_options)
    def closed(self,spider):
        self.bro.quit()
    def parse(self, response):
        print('parse start')
        li_list = response.xpath('//ul[@class="clearfix"]/li')
        target = [1,3,5]
        for index in target:
            target_url = 'https://pic.netbian.com' + li_list[index].xpath('./a/img/@src')[0].extract()
            self.target_urls.append(target_url)
        for url in self.target_urls:
            yield scrapy.Request(url,callback=self.parse_detail)
    def parse_detail(self,response):
        print(response.url)

