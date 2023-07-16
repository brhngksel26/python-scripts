from decorators import timer, async_timer
import requests
import aiohttp
import asyncio

url = 'https://dog.ceo/api/breeds/image/random'

@timer 
def sync_get_request():
    for _ in range(1, 151):
        resp = requests.get(url)
        random = resp.json()


async def _async_get_request(session, url):
    async with session.get(url) as resp:
        return await resp.json()

@async_timer
async def async_get_request():
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.ensure_future(_async_get_request(session, url)) for _ in range(1,151)
        ]
        return await asyncio.gather(*tasks)

asyncio.run(async_get_request())
sync_get_request()