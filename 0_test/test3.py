import json

import requests

# post
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 102.0.5005.63Safari / 537.36Edg / 102.0.1245.39'
    }
    url = 'https://fanyi.baidu.com/sug'
    # 表单数据
    data = {
        'kw': 'invoke',
    }
    response = requests.post(url=url, data=data, headers=headers)
    dic_obj = response.json()
    print(dic_obj)
    fp = open('invoke.json', 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
