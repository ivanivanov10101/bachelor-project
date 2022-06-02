import asyncio
import aiohttp
import csv
from asyncio_throttle import Throttler
import time

async def get(throttler, session: aiohttp.ClientSession, site: str):
    async with throttler:
        tic = time.perf_counter()
        url = f"https://www.{site}/"
        print(f"Requesting: {site}")
        resp = await session.request('GET', url=url)
        toc = time.perf_counter()
        time_taken = toc - tic
        print(f"Received: {site}")
        return time_taken


async def main(urls):
    tasks = []
    throttler = Throttler(rate_limit=100, period=15)
    async with aiohttp.ClientSession() as session:
        for c in urls:
            tasks.append(get(throttler, session=session, site=c))
        htmls = await asyncio.gather(*tasks, return_exceptions=True)
        print(htmls)
        with open('csv\\time_data.csv', "w", newline="") as f:
            writer = csv.writer(f)
            for i in htmls:
                writer.writerow([i])
        return htmls


if __name__ == '__main__':
    urls = []
    with open('main.csv', newline='') as file:
        for row in csv.reader(file):
            urls.append(row[1])
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main(urls))