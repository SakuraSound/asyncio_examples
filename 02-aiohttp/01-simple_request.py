import asyncio
import aiohttp

from datetime import datetime


async def simple_run(url):
    start = datetime.now().time()
    async with aiohttp.request("GET", url) as response:
        if response.status == 200:
            print(url, "T", len(await response.text()), start, datetime.now().time())
        else:
            print(url, "F", 0, start, datetime.now().time())


if __name__ == "__main__":
    print("Run basic async function.")
    # We first retrieve our event loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(simple_run("http://python.org"))
    print("Finished!")
