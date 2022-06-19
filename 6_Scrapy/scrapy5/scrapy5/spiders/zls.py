import scrapy
from scrapy5.items import Scrapy5Item
import pymysql as mysql
import requests
class ZlsSpider(scrapy.Spider):
    name = 'zls'
    start_urls = ['https://pic.netbian.com/4kmeinv/index.html']
    url = 'https://pic.netbian.com/4kmeinv/index_%s.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39'
    }
    page_num = 1
    conn = mysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='imgTest')
    cursor = conn.cursor()
    def parse(self, response):
        print(response)
        li_list = response.xpath('//ul[@class="clearfix"]/li')
        for li in li_list:
            img_src = 'https://pic.netbian.com' + li.xpath('./a/img/@src')[0].extract()
            img_name = li.xpath('./a/img/@alt')[0].extract() + '.jpg'
            img_data = requests.get(url=img_src, headers=self.headers).content
            self.cursor.execute("select count(*) as count from photo where url=%s",img_src)
            (check,)  = self.cursor.fetchone()
            print(check)
            if check == 0:
                item = Scrapy5Item()
                item['img_name'] = img_name
                item['img_src'] = img_src
                item['img_data'] = img_data
                yield item
            else:
                print('图片已爬取过')
        if self.page_num <= 3:
            self.page_num += 1
            new_url = format(self.url % str(self.page_num))
            yield scrapy.Request(url=new_url, callback=self.parse)