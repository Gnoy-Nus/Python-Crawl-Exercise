import asyncio
import time

#future对象
async def set_after(fut):
    await asyncio.sleep(1)
    fut.set_result('666')

async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    await loop.create_task(set_after(fut))
    data = await fut
    print(data)
start = time.time()
asyncio.run(main())
print(time.time()-start)