import os.path
import requests

# 提取多页面图片
if __name__ == '__main__':
    dir_name='./入门2'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 102.0.5005.63Safari / 537.36Edg / 102.0.1245.39'
    }
    url1 = 'https://m.qidian.com/majax/rank/yuepiaolist' #网页刷新的url
    url2 = 'https://bookcover.yuewen.com/qdbimg/349573/%s/150' #获取图片的url
    b_ids = []
    for page in range(1, 3):
        page = str(page)
        param = {
            '_csrfToken': 'IzTOnI3rF2mJAVCmQqZuh090y6lNla2ENQRflvok',  # 可能需要更新
            'gender': 'male',
            'pageNum': page,
            'catId': '-1',
            'yearmonth': '202205',
        }
        response = requests.get(url=url1, params=param, headers=headers)
        for dic_obj in response.json()['data']['records']:
            print(dic_obj)
            b_ids.append(dic_obj['bid'])
            img_src=format(url2%dic_obj['bid'])
            img_data = requests.get(url=img_src, headers=headers).content
            img_name = img_src.split('/')[-2]
            img_path = dir_name + '/' + img_name + '.jpg'
            with open(img_path, 'wb') as fp:
                fp.write(img_data)

