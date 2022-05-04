import sys
import os
import json
import asyncio
import aiohttp


# Initialize connection pool
conn = aiohttp.TCPConnector(limit_per_host=100, limit=0, ttl_dns_cache=300)
PARALLEL_REQUESTS = 100
results = []
urls = ['https://jsonplaceholder.typicode.com/todos/1' for i in range(4000)] #array of urls

async def gather_with_concurrency(n):
    semaphore = asyncio.Semaphore(n)
    session = aiohttp.ClientSession(connector=conn)

    # heres the logic for the generator
    async def get(url):
        async with semaphore:
            async with session.get(url, ssl=False) as response:
                obj = json.loads(await response.read())
                results.append(obj)
    await asyncio.gather(*(get(url) for url in urls))
    await session.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(gather_with_concurrency(PARALLEL_REQUESTS))
conn.close()

print(f"Completed {len(urls)} requests with {len(results)} results")