import asyncio
import aiohttp
import csv
from asyncio_throttle import Throttler

def parse(htmls):
    data = []
    for code in htmls:
        try:
            data.append([
                code['url'],
                code['green'],
                code['bytes'],
                code['cleanerThan'],
                code['statistics']['adjustedBytes'],
                code['statistics']['energy'],
                code['statistics']['co2']['grid']['grams'],
                code['statistics']['co2']['grid']['litres'],
                code['statistics']['co2']['renewable']['grams'],
                code['statistics']['co2']['renewable']['litres'],
                code['timestamp']
            ])
        except (KeyError, aiohttp.ContentTypeError) as e:
            print(f'File {file} is empty. Skipping.{e}')

    data.insert(0, ['URL', 'Green Hosting', 'Bytes', 'Cleaner Than %', 'Stats_Adjusted Bytes', 'Stats_Energy', 'Stats_CO2_Grid_Grams', 'Stats_CO2_Grid_Litres', 'Stats_CO2_Renewable_Grams', 'Stats_CO2_Renewable_Litres'])

    with open('csv\\database59400-59600.csv', "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)


async def get(throttler, session: aiohttp.ClientSession, site: str):
    async with throttler:
        url = f"https://api.websitecarbon.com/site?url={site}/"
        print(f"Requesting: {site}")
        resp = await session.request('GET', url=url)
        data = await resp.json(content_type='application/json')
        print(f"Received: {site}")
        return data


async def main(urls):
    tasks = []
    throttler = Throttler(rate_limit=50, period=15)
    async with aiohttp.ClientSession() as session:
        for c in urls:
            tasks.append(get(throttler, session=session, site=c))
        htmls = await asyncio.gather(*tasks, return_exceptions=True)
        parse(htmls)
        return htmls


if __name__ == '__main__':
    urls = []
    with open('test_data.csv', newline='') as file:
        for row in csv.reader(file):
            urls.append(row[0])
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main(urls))