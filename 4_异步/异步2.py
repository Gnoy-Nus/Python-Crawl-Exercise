import asyncio

async def request(url):
    print('正在下载:',url)
    return url

c=request('www.baidu.com') #返回协程对象

#基本使用
# loop = asyncio.get_event_loop() #创建事件循环对象
# #协程对象注册到loop中，启动loop
# loop.run_until_complete(c)


# #task使用
# loop = asyncio.get_event_loop()
# task = loop.create_task(c)
# loop.run_until_complete(task)

# #future使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# loop.run_until_complete(task)

#绑定回调
def call_back(task):
    print(task.result())
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
task.add_done_callback(call_back)
loop.run_until_complete(task)


