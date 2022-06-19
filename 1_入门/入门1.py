import os.path
import re

import requests

# 提取页面图片，正则解析
if __name__ == '__main__':
    if not os.path.exists('./入门1'):
        os.mkdir('./入门1')
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 102.0.5005.63Safari / 537.36Edg / 102.0.1245.39'
    }
    url = 'https://m.qidian.com/rank/yuepiao/'
    response = requests.get(url=url, headers=headers)
    page_text = response.text
    ex = '<li class="book-li">.*?<img src=".*?" data-src="(.*?)" class="book-cover" alt.*?</li>'
    img_src_list = re.findall(ex, page_text, re.S)
    print(img_src_list)
    for src in img_src_list:
        src = 'https:' + src
        print(src)
        img_data = requests.get(url=src, headers=headers).content
        img_name = src.split('/')[-2]
        img_path = './入门1/' + img_name + '.jpg'
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
