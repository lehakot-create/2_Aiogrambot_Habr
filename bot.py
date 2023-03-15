import asyncio
import logging
from aiogram import Bot, Dispatcher

from settings import config
from handlers import group_games, different_types, questions


logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=config.TOKEN)
    dp = Dispatcher()
    dp.include_routers(questions.router, different_types.router)
    dp.include_router(group_games.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
