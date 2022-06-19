from bs4 import BeautifulSoup
import requests
# bs4
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 102.0.5005.63Safari / 537.36Edg / 102.0.1245.39'
    }
    url = 'https://m.qidian.com/book/1027339371/catalog/'
    page_text = requests.get(url=url,  headers=headers).text
    soup = BeautifulSoup(page_text,'lxml')
    li_list = soup.select('.chapter-li.jsChapter.auto-report')
    fp = open('入门3.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.h2.a.span.string
        detail_url= 'https:'+li.h2.a['href']
        detail_page_text = requests.get(url=detail_url,headers=headers).text
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        c_id = 'c_' + li.h2.a['href'].split('/')[-1][:-5]
        div_tag = detail_soup.find('div', id=c_id)
        content = div_tag.text
        fp.write(title+':'+content+'\n')

