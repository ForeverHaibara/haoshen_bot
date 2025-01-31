# -*- coding: utf-8 -*-
"""
@author: zyckk4  https://github.com/zyckk4
"""

from utils.utils import Listen, send
import aiohttp


@Listen.all_mesg()
async def github_zen(event):
    if str(event.message_chain) == '/zen':
        try:
            zen = await get_zen()
        except:
            await send(event, "获取zen失败！")
            return
        await send(event, zen)


async def get_zen(timeout=10):
    url = 'https://api.github.com/zen'
    timeout = aiohttp.ClientTimeout(total=timeout)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(url=url) as resp:
            return await resp.text()

if __name__ == '__main__':
    import asyncio
    asyncio.run(get_zen())
