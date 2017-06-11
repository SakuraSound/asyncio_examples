import asyncio

import uvloop
from sanic import Sanic
from sanic.response import text

app = Sanic("hello_sanic")


@app.route("/sync")
def hello_sync(request):
    # your endpoints can be synchronous or asynchronous
    # Though if synchronous, you cant use asyncio constructs
    return text("Hello Sanic sync!")


@app.route("/async")
async def hello_async(request):
    return text("Hello Sanic async!")


if __name__ == "__main__":
    # Use uvloop cause its fast!
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    app.run(host="0.0.0.0", port=9090)
