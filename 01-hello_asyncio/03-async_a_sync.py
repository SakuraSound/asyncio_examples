import asyncio
import requests


# Async descriptor defines this fucntion as a coroutine
async def run():
    loop = asyncio.get_event_loop()
    print("Accessing ibm.com")
    # Run in executor defaults to ThreadPoolExecutor if None is given
    # This will take our synchronous code, and wrap it in a thread/process
    # And will return a future when our sync code completes.
    result = await loop.run_in_executor(None, requests.get, "http://www.ibm.com")
    print("Status Code", result.status_code)
    print("Body Length", len(result.text))


if __name__ == "__main__":
    print("Run basic async function.")
    # We first retrieve our event loop
    loop = asyncio.get_event_loop()
    # Then we pass our coroutine to be executed on the event loop
    loop.run_until_complete(run())
    print("Finished!")
