import asyncio
import logging
from aiogram import Bot, Dispatcher

from settings import config
from handlers import group_games, different_types, handler_commands
from handlers.handler_main import HandlerMain


logging.basicConfig(level=logging.INFO)


class MainBot:
    def __init__(self):
        self.token = config.TOKEN
        self.bot = Bot(self.token)
        self.handler = HandlerMain(self.bot)
        self.dp = Dispatcher()

    def start(self):
        self.dp.include_routers(self.handler.handler_commands.router)
        logging.info('Bot started')
        self.handler.handle()

    async def run_bot(self):
        self.start()
        await self.dp.start_polling(self.bot)


# async def main():
#     bot = Bot(token=config.TOKEN)
#     dp = Dispatcher()
#     dp.include_routers(questions.router, different_types.router)
#     dp.include_router(group_games.router)

#     await bot.delete_webhook(drop_pending_updates=True)
#     await dp.start_polling(bot)


async def main():
    bot = MainBot()
    bot.bot.delete_webhook()
    await bot.run_bot()

    # dp = Dispatcher()
    # await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
