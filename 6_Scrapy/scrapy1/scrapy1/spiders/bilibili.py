import scrapy
from scrapy1.items import Scrapy1Item
import os
import requests

class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    # allowed_domains = ['www.bilibili.com'] #用域名限制start_urls中执行爬虫的url
    start_urls = ['https://pic.netbian.com/4kmeinv/index.html']
    url = 'https://pic.netbian.com/4kmeinv/index_%s.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39'
    }
    page_num = 1

    # def parse_detail(selfs,response):
    #     item = response.meta['item']
    #     ...
    #     yield item
    def parse(self, response):
        print(response)
        dir_name = './result'
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        li_list = response.xpath('//ul[@class="clearfix"]/li')
        # 解析单页
        for li in li_list:
            img_src = 'https://pic.netbian.com' + li.xpath('./a/img/@src')[0].extract()
            img_name = li.xpath('./a/img/@alt')[0].extract() + '.jpg'
            img_path = dir_name + '/' + img_name
            img_data = requests.get(url=img_src, headers=self.headers).content
            # yield scrapy.Request(url=img_src, callback=self.parse_detail,meta={'item':item}) #若需要继续解析子url，用此方法，meta属性传递item
            # 封装到item中
            item = Scrapy1Item()
            item['img_path'] = img_path
            item['img_data'] = img_data
            #提交到管道
            yield item
        # 分页继续解析
        if self.page_num<=3:
            self.page_num+=1
            new_url=format(self.url%str(self.page_num))
            yield scrapy.Request(url=new_url,callback=self.parse)