import asyncio
import aiohttp
from datetime import datetime


# Async descriptor defines this fucntion as a coroutine
async def run(urls):
    loop = asyncio.get_event_loop()
    print("Accessing some websites")
    # These requests are done asynchrnously... in that other coroutines can operate while this one
    # waits for IO to complete. This is still running sequentially though, since we are iterating one
    # URL at a time...

    # We create our ClientSession object to perform reqeust operations.
    async with aiohttp.ClientSession(loop=loop) as session:
        start = datetime.now().time()
        for i, url in enumerate(urls):
            async with session.get(url) as response:
                if response.status == 200:
                    print(url, "T", len(await response.text()), start, datetime.now().time())
                else:
                    print(url, "F", 0, start, datetime.now().time())


async def simple_run(url):
    start = datetime.now().time()
    async with aiohttp.request("GET", "http://python.org") as response:
        if response.status == 200:
            print(url, "T", len(await response.text()), start, datetime.now().time())
        else:
            print(url, "F", 0, start, datetime.now().time())


if __name__ == "__main__":
    print("Run basic async function.")
    # We first retrieve our event loop
    loop = asyncio.get_event_loop()
    urls = ["http://www.ibm.com", "http://www.google.com", "http://www.amazon.com", "http://www.microsoft.com"]
    # Then we pass our coroutine to be executed on the event loop
    group = asyncio.gather(*[simple_run("http://python.org"), run(urls), simple_run("http://mainichi.jp")])
    loop.run_until_complete(group)
    print("Finished!")
