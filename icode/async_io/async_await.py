import asyncio
from datetime import datetime

@asyncio.coroutine
def hello():
    print('Hello world', datetime.now())
    yield from asyncio.sleep(1)
    print('Htllo again!', datetime.now())


# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()


def hello2():
    print('Hello world', datetime.now())
    yield from asyncio.sleep(1)
    print('Htllo again!', datetime.now())


loop2 = asyncio.get_event_loop()
tasks = [hello2(),hello2(),hello2(),hello2(),hello2()]
loop2.run_until_complete(asyncio.wait(tasks))
loop2.close()