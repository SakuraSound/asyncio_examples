import asyncio
import random


# Async descriptor defines this fucntion as a coroutine
async def work_it(i, random_sleep):
    # Await descriptor defines explicit context switch location in code
    await asyncio.sleep(random_sleep)
    print("Task {0} completed after random sleep of {1} seconds".format(i, random_sleep))


if __name__ == "__main__":
    print("Run basic async function.")
    # We first retrieve our event loop
    loop = asyncio.get_event_loop()
    # Then we pass our coroutine to be executed on the event loop
    loop.run_until_complete(work_it(1, random.randrange(1, 5)))
    print("Finished!")
