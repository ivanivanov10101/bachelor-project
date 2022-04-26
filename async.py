import asyncio
import aiohttp  # pip install aiohttp aiodns
import csv
import json

async def get(
    session: aiohttp.ClientSession,
    site: str,
    **kwargs
) -> dict:
    url = f"https://api.websitecarbon.com/site?url={site}/"
    print(f"Requesting {url}")
    resp = await session.request('GET', url=url, **kwargs)
    # Note that this may raise an exception for non-2xx responses
    # You can either handle that here, or pass the exception through
    data = await resp.json()
    print(f"Received data for {url}")
    with open(f'json\\{site}.json', 'w+') as f:
        json.dump(data, f)
    return data


async def main(urls, **kwargs):
    # Asynchronous context manager.  Prefer this rather
    # than using a different session for each GET request
    async with aiohttp.ClientSession() as session:
        tasks = []
        for c in urls:
            tasks.append(get(session=session, site=c, **kwargs))
        # asyncio.gather() will wait on the entire task set to be
        # completed.  If you want to process results greedily as they come in,
        # loop over asyncio.as_completed()
        htmls = await asyncio.gather(*tasks, return_exceptions=True)
        return htmls


if __name__ == '__main__':
    urls = []
    with open('test_data.csv', newline='') as inputfile:
        for row in csv.reader(inputfile):
            urls.append(row[0])
    # Either take urls from stdin or make some default here
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main(urls))  # Python 3.7+
    