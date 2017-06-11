import asyncio
import random


async def next_k_sprites(k, sprites):
    for i in range(k):
        # Simulating blocking call (DB? Service?)
        await asyncio.sleep(1)
        pos = random.randint(0, len(sprites) - 1)
        yield sprites[pos]
        # This final one is required
        await asyncio.sleep(0)


async def run():
    sprites = ["bonbon", "taffy", "mochi", "cookie", "cake", "ice_cream"]
    async for sprite in next_k_sprites(50, sprites):
        print(sprite)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
