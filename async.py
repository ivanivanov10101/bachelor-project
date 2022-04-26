import asyncio
import aiohttp
import csv
import json

async def get(session: aiohttp.ClientSession, site: str):
    url = f"https://api.websitecarbon.com/site?url={site}/"
    print(f"Requesting {url}")
    resp = await session.request('GET', url=url)
    data = await resp.json()
    print(f"Received data for {url}")
    with open(f'json\\{site}.json', 'w+') as f:
        json.dump(data, f)
    return data


async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for c in urls:
            tasks.append(get(session=session, site=c))
        htmls = await asyncio.gather(*tasks, return_exceptions=True)
        return htmls


if __name__ == '__main__':
    urls = []
    with open('test_data.csv', newline='') as file:
        for row in csv.reader(file):
            urls.append(row[0])
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main(urls))
    