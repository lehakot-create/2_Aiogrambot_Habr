import asyncio
import logging
from aiogram import Bot, Dispatcher

from settings import config
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


async def main():
    bot = MainBot()
    await bot.bot.delete_webhook()
    await bot.run_bot()


if __name__ == "__main__":
    asyncio.run(main())
