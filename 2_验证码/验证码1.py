import requests
from lxml import etree
from PIL import Image
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39'
    }
    url = 'https://so.gushiwen.cn/user/login.aspx'
    response = requests.get(url=url, headers=headers)
    page_text = response.text
    tree = etree.HTML(page_text)
    code_img_src='https://so.gushiwen.cn'+tree.xpath('// *[ @ id = "imgCode"]/@src')[0]
    img_data = requests.get(url=code_img_src,headers=headers).content
    with open('./code.jpg', 'wb') as fp:
        fp.write(img_data)
    fp.close()
    code_img = Image.open("code.jpg")  # 读入图像
    code_img.show()
    code = input('人工输入验证码：')