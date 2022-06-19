
import requests


if __name__ == '__main__':
    url = 'https://www.baidu.com/s?wd=IP'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39'
    }
    response = requests.get(url=url,headers=headers) #直接设置全局代理则此处不需要加proxies参数
    # response = requests.get(url=url, headers=headers, proxies={"https": "139.162.71.149:22104"})
    page_text = response.text
    print(page_text)
    with open('ip.html','w',encoding='utf-8') as fp:
        fp.write(page_text)