import asyncio
import time
import aiohttp
#aiohttp基于异步网络请求发送
#需先运行flask_simulation.py模拟网络
urls = [
    'http://127.0.0.1:5000/sun',
    'http://127.0.0.1:5000/yong',
]
start = time.time()
async def get_page(url):
    print('正在下载:', url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text() #一定要用await
            print('下载完成:', text)


stasks = []
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(stasks))
print(time.time() - start)