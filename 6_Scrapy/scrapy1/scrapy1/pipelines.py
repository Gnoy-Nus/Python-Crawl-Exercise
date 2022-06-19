# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql as mysql

class Scrapy1Pipeline:
    # fp = None
    # def open_spider(self,spider):
    #     print('开始爬虫')
    #     self.fp = open('./result.txt','w',encoding='utf-8')
    # def close_spider(self,spider):
    #     print('结束爬虫')
    #     self.fp.close()
    def process_item(self, item, spider):
        print('调用pipeline\n')
        img_data = item['img_data']
        img_path = item['img_path']
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
        # self.fp.write(input_raw,'\n',input_extract)
        return item  #传递给下一个Pipeline


class mysqlPipeline:
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = mysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',db='imgTest')
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
    def process_item(self, item, spider):
        print('调用mysql的pipeline\n')
        self.cursor=self.conn.cursor()
        try:
            # self.cursor.execute("Insert into photo(src) values(%s)", (mysql.Binary(img)))
            self.cursor.execute("Insert into photo(src) values(%s)",item['img_data'])
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item