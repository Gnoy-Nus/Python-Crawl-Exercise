import requests


#UA伪装
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 102.0.5005.63Safari / 537.36Edg / 102.0.1245.39'
    }
    url = 'https://baidu.com/s'
    kw=input('enter a word:')
    param={
        'wd':kw
    }
    response = requests.get(url=url,params=param,headers=headers)
    page_text = response.text
    print(page_text)
    file_name=kw+'.html'
    with open(file_name,'w',encoding='utf-8') as fp:
        fp.write(page_text)