import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiohttp import web
from aiogram.types import Update


from settings import config
from handlers.handler_main import HandlerMain


logging.basicConfig(level=logging.INFO)


class MainBot:
    def __init__(self):
        self.token = config.TOKEN
        self.bot = Bot(self.token)
        self.handler = HandlerMain(self.bot)
        self.dp = Dispatcher()

    # def start(self):
    #     self.dp.include_routers(self.handler.handler_commands.router,
    #                             self.handler.handler_all_text.router,
    #                             self.handler.handler_inline_query.router)
    #     self.handler.handle()
    #     logging.info('Bot started')

    # async def run_bot(self):
    #     self.start()
    #     await self.dp.start_polling(self.bot)

    async def on_startup(self, app):
        self.dp.include_routers(self.handler.handler_commands.router,
                                self.handler.handler_all_text.router,
                                self.handler.handler_inline_query.router)
        self.handler.handle()
        # устанавливаем webhook
        await self.bot.set_webhook(
            f"https://{config.WEBHOOK_HOST}/{config.TOKEN}"
            )
        # сообщаем, что бот запущен
        print("Бот запущен. Webhook установлен.")

    async def on_shutdown(self, app):
        # удаляем webhook
        await self.bot.delete_webhook()
        # закрываем соединение с ботом
        await self.bot.close()
        # сообщаем, что бот остановлен
        print("Бот остановлен.")

    async def on_update(self, app, update: Update):
        # обрабатываем обновление
        await self.dp.process_update(update)


# async def main():
#     bot = MainBot()
#     await bot.bot.delete_webhook()
#     await bot.run_bot()


# if __name__ == "__main__":
#     asyncio.run(main())


if __name__ == "__main__":
    bot = MainBot()
    # await bot.bot.delete_webhook()
    # await bot.run_bot()
    # создаем объект приложения aiohttp
    app = web.Application()
    # добавляем обработчик для входящих обновлений
    app.on_post("/webhook_url")(bot.on_update)
    # запускаем бота
    web.run_app(app,
                host="localhost",
                port=8080,
                access_log=False,
                startup_app=bot.on_startup,
                shutdown_app=bot.on_shutdown)
