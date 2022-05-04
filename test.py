import aiohttp
import asyncio
import time

start_time = time.time()


async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json(content_type='None')
        return pokemon['name']


async def main():

    async with aiohttp.ClientSession() as session:

        tasks = []
        url = 'https://api.websitecarbon.com/site?url=calendly.com/'
        tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))