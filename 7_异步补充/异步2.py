import asyncio

#asyncio\async\await基本使用
async def func1():
    print('func1()执行')
    await asyncio.sleep(3)
    print('func1()完成')
    return 1


async def func2():
    print('func2()执行')
    await asyncio.sleep(1)
    print('func2()完成')
    return 2

async def main():
    print('main')
    # task1=asyncio.create_task(func1())
    # task2 = asyncio.create_task(func2())
    # response1 = await task1
    # response2 = await task2
    # print(response1, response2)
    tasks = [
        asyncio.create_task(func1(),name='t1'),
        asyncio.create_task(func2(),name='t2')
    ]
    done,pending = await asyncio.wait(tasks,timeout=None)
    print(done)
    print(pending)


# tasks = [
#     asyncio.ensure_future(func1()),
#     asyncio.ensure_future(func2())
# ]
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))

asyncio.run(main())


# tasks = [
#     func1(),
#     func2()
# ]
# asyncio.run(asyncio.wait(tasks,timeout=None))