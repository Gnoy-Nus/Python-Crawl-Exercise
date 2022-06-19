# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql as mysql
class mysqlPipeline:
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = mysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',db='imgTest')
        self.cursor = self.conn.cursor()
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
    def process_item(self, item, spider):
        print('调用mysql的pipeline\n')
        try:
            self.cursor.execute("Insert into photo(src,url,name) values(%s,%s,%s)",(item['img_data'],str(item['img_src']),str(item['img_name'])))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item