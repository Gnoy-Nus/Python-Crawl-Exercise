import scrapy
from scrapy2.items import Scrapy2Item

class ImgspiderSpider(scrapy.Spider):
    name = 'imgSpider'
    start_urls = ['https://pic.netbian.com/4kmeinv/index.html']
    url = 'https://pic.netbian.com/4kmeinv/index_%s.html'
    page_num = 1
    def parse(self, response):
        print(response)
        li_list = response.xpath('//ul[@class="clearfix"]/li')
        for li in li_list:
            img_src = 'https://pic.netbian.com' + li.xpath('./a/img/@src')[0].extract()
            img_name = li.xpath('./a/img/@alt')[0].extract() + '.jpg'
            item = Scrapy2Item()
            item['img_name'] =img_name
            item['img_src'] = img_src
            yield item
        if self.page_num<=3:
            self.page_num+=1
            new_url=format(self.url%str(self.page_num))
            yield scrapy.Request(url=new_url,callback=self.parse)