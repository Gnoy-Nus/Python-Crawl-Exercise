from lxml import etree
import requests

# xpath解析榜单
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 102.0.5005.63Safari / 537.36Edg / 102.0.1245.39'
    }
    url = 'https://m.qidian.com/rank/'
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="module module-toplist"]//li')
    fp = open('入门4.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.xpath('./a/h2/text()')[0]
        rank = li.xpath('./a/h2/@title')[0]
        fp.write(rank + ' ' + title + '\n')
