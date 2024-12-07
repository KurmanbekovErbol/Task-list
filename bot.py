import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from app.handlers import router
from config import token

bot = Bot(token=token)
dp = Dispatcher()

async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_routers(router)
    await dp.start_polling(bot)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Выход")