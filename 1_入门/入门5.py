from lxml import etree
import requests
import os
# xpath解析+乱码解决+图片爬取
if __name__ == '__main__':
    dir_name = './入门5'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39'
    }
    for page in range(1,3):
        url = 'https://pic.netbian.com/4kmeinv/index_%s.html'
        page =str(page)
        url = format(url%page)
        response = requests.get(url=url, headers=headers)
        # response.encoding = 'utf-8'
        page_text = response.text
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//ul[@class="clearfix"]/li')
        for li in li_list:
            img_src = 'https://pic.netbian.com'+li.xpath('./a/img/@src')[0]
            img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
            img_name = img_name.encode('iso-8859-1').decode('gbk')
            img_path = dir_name + '/' + img_name
            img_data = requests.get(url=img_src,headers=headers).content
            with open(img_path, 'wb') as fp:
                fp.write(img_data)
