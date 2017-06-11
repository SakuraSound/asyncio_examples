import asyncio


class PlayerState():

    __db__ = {
        "player_state__US": {
            "SakuraSound": {}
        }
    }

    async def get_lock(self, player_id):
        # simulating IO
        await asyncio.sleep(1)
        return True

    async def unlock(self):
        await asyncio.sleep(2)
        return None

    async def update_state(self, key, value):
        self.state[key] = value

    def __init__(self, player_id, region='US'):
        self.loop = asyncio.get_event_loop()
        self.player_id = player_id
        self.region = region

    async def __aenter__(self):
        self.lock = await self.get_lock(self.player_id)
        self.state = await self.loop.run_in_executor(None, self.get_state, self.player_id)
        print("locking {0}".format(self.player_id))
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if hasattr(self, 'lock'):
            if hasattr(self, 'lock'):
                await self.loop.run_in_executor(None, self.push_state)
            await self.unlock()
        else:
            raise AssertionError("Did we have the lock?")

    def get_state(self, player_id):
        # Cloudant api extends dict object (searches perform I/O)
        coll_name = "__".join(["player_state", self.region])
        collection = PlayerState.__db__[coll_name]
        return collection[player_id]

    def push_state(self):
        PlayerState.__db__.update(self.state)


async def run(player):
    async with PlayerState(player) as ps:
        await ps.update_state("foo", "bar")
        print(ps.state)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run("SakuraSound"))
