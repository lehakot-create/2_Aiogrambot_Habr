from aiogram import Router, F
from aiogram.types import Message

from handlers.handler import Handler


class HandlerAllText(Handler):
    def __init__(self, bot):
        super().__init__(bot)
        self.router = Router()

    async def get_my_subscribe(self, user_id: int, message: Message):
        """
        Получает подписки пользователя
        """
        result = self.DB.get_user_subscribe(user_id)
        if not result:
            all_themes = self.DB.get_all_themes()
            await message.answer('У вас нет подписок.\nВыберите из списка ниже',
                           reply_markup=self.inline_kb.inline_list_themes(
                                all_themes)
                           )
            """
            запустить сбор подписок и вернуть возможные варианты
            """

        else:
            """
            вернуть из бд все подписки пользователя
            """
            print('ok')

    def handle(self):
        @self.router.message(F.text)
        async def get_news(message: Message):
            if message.text == 'Получить новости':
                await message.answer('Раздел новостей в разработке',
                                     reply_markup=self.kb.main_kb())
            elif message.text == 'Мои подписки':
                await message.answer('Раздел подписки в разработке',
                                     reply_markup=self.kb.main_kb())
                await self.get_my_subscribe(
                    user_id=message.from_user.id, message=message
                    )
