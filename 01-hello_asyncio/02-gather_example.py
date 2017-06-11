import asyncio
import random


# Async descriptor defines this fucntion as a coroutine
async def work_it(i, random_sleep):
    # Await descriptor defines explicit context switch location in code
    await asyncio.sleep(random_sleep)
    print("Task {0} completed after random sleep of {1} seconds".format(i, random_sleep))


if __name__ == "__main__":
    print("asyncio.gather example.")
    # We first retrieve our event loop
    loop = asyncio.get_event_loop()
    futures = [work_it(i, random.randrange(1, 5)) for i in range(0, 10)]
    # gather takes a group of coroutines, runs them, with a single awaitable future
    group_future = asyncio.gather(*futures)
    # Then we pass our coroutine to be executed on the event loop
    loop.run_until_complete(group_future)
    print("Finished!")
