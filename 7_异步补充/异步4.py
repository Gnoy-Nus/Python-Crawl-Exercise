import asyncio
import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor

def func(value):
    print(value)
    time.sleep(1)
    return 123
async def main():
    loop = asyncio.get_running_loop()
    value= 5
    # fut = loop.run_in_executor(None,func) #第三方模块不支持基于协程的异步时使用run_in_executor
    # result = await fut
    # print(result)
    with ThreadPoolExecutor() as Pool:
        result = await loop.run_in_executor(Pool, func,value) #第三方模块不支持基于协程的异步时使用run_in_executor
        print(result)
asyncio.run(main())

# if __name__ == '__main__':
#     Pool = ThreadPoolExecutor(max_workers=5)
#     Pool = ProcessPoolExecutor(max_workers=5)
#     for i in range(10):
#         fut = Pool.submit(func,i)
#         print(fut)

#以下函数可以在class中定义，异步调用类的方法比如：async with className as f:
## async def __aenter__
## async def __aexit__


