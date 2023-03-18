from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters.text import Text

from handlers.handler import Handler
from keyboards.inline_keyboard import NumbersCallbackFactory


class HandlerInlineQuery(Handler):
    def __init__(self, bot):
        super().__init__(bot)
        self.router = Router()

    def handle(self):
        @self.router.callback_query(NumbersCallbackFactory.filter())
        async def call_inline(callback: CallbackQuery,
                              callback_data: NumbersCallbackFactory):
            await callback.message.answer(f'{callback_data.id}')
            self.DB.add_theme_to_my_subscribe(
                id_theme=callback_data.id,
                user_id=callback.message.from_user.id
                )
            await callback.answer()
