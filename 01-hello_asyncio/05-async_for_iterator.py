import asyncio
import random


class NextSprite(object):

    __sprites__ = ["bonbon", "taffy", "mochi", "cookie", "cake"]

    def __init__(self, to):
        self.curr = 0
        self.to = to

    async def __anext__(self):
        if self.curr >= self.to:
            raise StopAsyncIteration
        self.curr += 1
        i = random.randint(0, len(NextSprite.__sprites__) - 1)
        await asyncio.sleep(1)
        return NextSprite.__sprites__[i]

    async def __aiter__(self):
        return self

    @classmethod
    async def get_next_k(cls, k):
        async for sprite in NextSprite(k):
            print(sprite)


loop = asyncio.get_event_loop()
loop.run_until_complete(NextSprite.get_next_k(30))
