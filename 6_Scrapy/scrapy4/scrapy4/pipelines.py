# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as mysql

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Scrapy4Pipeline:
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = mysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',db='books')
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
    def process_item(self, item, spider):
        self.cursor=self.conn.cursor()
        try:
            if item.__class__.__name__ == 'BookItem':
                # print('book_url', item['book_url'])
                pass
            else:
                book_id = item['chapter_url'].split('/')[-2]
                self.cursor.execute("Insert into chapters (`b_id`,`c_url`) values(%s,%s)",(book_id,str(item['chapter_url'])))
                print('chapter_url', item['chapter_url'])
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item


