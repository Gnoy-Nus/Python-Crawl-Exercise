import requests
from lxml import etree
#csdn登录
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39'
    }
    url = 'https://passport.csdn.net/v1/register/pc/login/doLogin'  #csdn的登录url
    data = {
        'loginType': "1",
        'pwdOrVerifyCode': "xxxxxxxxx", #需填入
        'uaToken': "",
        'userIdentification': "xxxxxxxxx", #需填入
        'webUmidToken': ""
    }
    response = requests.post(url=url, data=data,headers=headers)
    print(response.status_code) #200表示登录成功


