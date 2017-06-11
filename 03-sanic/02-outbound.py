import asyncio

import aiohttp
import uvloop
from sanic import Sanic
from sanic.response import json

app = Sanic("hello_sanic")


@app.route("/ibm")
async def ibm(request):
    site = "http://www.ibm.com"
    response = await aiohttp.request("GET", site)
    return json({"website": site, "size": len(await response.text())})


if __name__ == "__main__":
    # Use uvloop cause its fast!
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    app.run(host="0.0.0.0", port=9090)
