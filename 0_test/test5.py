import json

import requests

# 多页爬虫
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 102.0.5005.63Safari / 537.36Edg / 102.0.1245.39'
    }
    url = 'https://m.qidian.com/majax/rank/yuepiaolist'
    records=[]
    for page in range(1,5):
        page = str(page)
        param = {
            '_csrfToken': 'IzTOnI3rF2mJAVCmQqZuh090y6lNla2ENQRflvok',  #可能需要更新
            'gender': 'male',
            'pageNum': page,
            'catId': '-1',
            'yearmonth': '202205',
        }
        response = requests.get(url=url, params=param, headers=headers)
        for dic_obj in response.json()['data']['records']:
            records.append(dic_obj)
    fp = open('yuepiao.json', 'w', encoding='utf-8')
    json.dump(records, fp=fp, ensure_ascii=False)

