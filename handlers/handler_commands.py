from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from handlers.handler import Handler


class HandlerCommands(Handler):
    def __init__(self, bot):
        super().__init__(bot)
        self.router = Router()

    def handle(self):
        @self.router.message(Command('start'))
        async def cmd_start(message: Message):
            await message.answer(f'Welcome {message.from_user.username}!!!',
                                 reply_markup=self.kb.main_kb())
            self.DB.add_user(user_telegram_id=message.from_user.id,
                             username=message.from_user.username,
                             first_name=message.from_user.first_name,
                             full_name=message.from_user.full_name)
