import requests

url1 = 'https://upos-sz-mirrorcoso1.bilivideo.com/upgcxcode/11/76/731187611/731187611_nb2-1-30120.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1655368947&gen=playurlv2&os=coso1bv&oi=2073615624&trid=c4773ded052641788fa74a1dc1aba676u&mid=50030956&platform=pc&upsig=ffdc34a7a84a4d5815128ddc0f9adb0b&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=1529935&logo=80000000'
url2 = 'https://upos-sz-mirrorcoso1.bilivideo.com/upgcxcode/11/76/731187611/731187611_nb2-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1655368947&gen=playurlv2&os=coso1bv&oi=2073615624&trid=c4773ded052641788fa74a1dc1aba676u&mid=50030956&platform=pc&upsig=0cf40a52a29eb4d4d5fa312f7a65385e&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=39771&logo=80000000'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.41',
    'Referer': 'https://www.baidu.com/',  # 此处可以是任意的网址,表示请求发起的来源页面
}
#分别获取音频和视频
session = requests.session()
res1 = session.get(url=url1, headers=headers)
res2 = session.get(url=url2, headers=headers)
print(res1,res2)
with open('p1.mp4', 'wb') as fp:
    fp.write(res1.content)
    fp.flush()
    fp.close()
with open('p2.mp4', 'wb') as fp:
    fp.write(res2.content)
    fp.flush()
    fp.close()

# 合并两个视频,需安装ffmpeg,https://blog.csdn.net/HYEHYEHYE/article/details/122000352
import os
file1 = "p1.mp4"
file2 = "p2.mp4"
result = "output.mp4"
print(os.system(f"ffmpeg.exe -i {file1} -i {file2} -vcodec copy -acodec copy {result}"))

