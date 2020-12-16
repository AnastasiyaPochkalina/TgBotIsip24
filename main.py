import asyncio
import aiohttp

from aiogram import Bot, Dispatcher, executor
from config import API_TOKEN

PROXY_URL = 'socks5://138.68.161.14:1080'

loop = asyncio.get_event_loop()
bot = Bot(token=API_TOKEN, proxy=PROXY_URL, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
	from handlers import dp, send_to_admin
	executor.start_polling(dp, on_startup=send_to_admin)
