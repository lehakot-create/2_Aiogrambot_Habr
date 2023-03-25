from aiogram import Router
from aiogram.types import CallbackQuery
from magic_filter import F

from handlers.handler import Handler
from keyboards.inline_keyboard import NumbersCallbackFactory


class HandlerInlineQuery(Handler):
    def __init__(self, bot):
        super().__init__(bot)
        self.router = Router()

    def handle(self):
        @self.router.callback_query(
                NumbersCallbackFactory.filter(F.action == 'add'))
        async def call_inline(callback: CallbackQuery,
                              callback_data: NumbersCallbackFactory):
            await self.DB.add_theme_to_my_subscribe(
                callback=callback,
                callback_data=callback_data,
                )
            await callback.answer()

        @self.router.callback_query(
                NumbersCallbackFactory.filter(F.action == 'delete'))
        async def call_inline_del_user_theme(
                callback: CallbackQuery,
                callback_data: NumbersCallbackFactory):
            await callback.message.answer(
                f'Вы отписались от {callback_data.title}')

            self.DB.delete_theme_to_my_subscribe(
                id_theme=callback_data.id,
                user_telegram_id=callback.from_user.id
                )
            await callback.answer()
