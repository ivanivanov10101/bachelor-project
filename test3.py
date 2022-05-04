import aiohttp
import asyncio
import json

test_url = "https://stackoverflow.com/"

def Logger(json_message):
    print(json.dumps(json_message))

async def get_data(url):
    Logger({"start": "get_data()", "url": url})
    if url is test_url: #This is a test to make "test url" sleep longer than the timeout.   
        await asyncio.sleep(2) 

    timeout = aiohttp.ClientTimeout(total=0.5) # TODO - timeout after half a second.
    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as results:            
                Logger({"finish": "get_data()", "url": url})
                return f"{ results.status } - {url}"
    except Exception as exc:
        Logger({"error": "get_data()", "url": url, "message": str(exc) })
        return f"fail - {url}"

async def main():
    urls = [test_url]*5 # create array of 5 urls
    urls[2] = "https://localhost:44344/" # Set third url to something that will timeout (after 0.5 sec).
    statements = [get_data(x) for x in urls]    
    Logger({"start": "gather()"})

    results = await asyncio.gather(*statements) 
    Logger({"finish": "gather()"})
    Logger({"results": ", ".join(results)})

if __name__ == '__main__':
    #asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # Use this to stop "Event loop is closed" error on Windows - https://github.com/encode/httpx/issues/914
    asyncio.run(main())