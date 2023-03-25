from aiogram import Router, F
from aiogram.types import Message

from handlers.handler import Handler
from utils.parser_habr_news import get_habr_news


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
        else:
            user_subscribe = self.DB.get_user_subscribe(user_id)
            await message.answer('Ваши подписки',
                                 reply_markup=self.inline_kb.user_inline_list_themes(
                                    user_subscribe
                                 ))

    async def get_my_news(self, message: Message):
        my_themes = self.DB.get_user_subscribe(message.from_user.id)
        for theme in my_themes:
            print(theme.id, theme.title, theme.url)
            my_news = get_habr_news(url_theme=theme.url)
            for el in my_news:
                await message.answer(f"{el.get('title')}\n https://habr.com{el.get('url')}",
                                     parse_mode='HTML')

    def handle(self):
        @self.router.message(F.text)
        async def get_news(message: Message):
            if message.text == 'Получить новости':
                await self.get_my_news(message)
                # await message.answer('Раздел новостей в разработке',
                #                      reply_markup=self.kb.main_kb())
            elif message.text == 'Все темы':
                await message.answer('Доступные темы',
                                     reply_markup=self.inline_kb.inline_list_themes(
                                        self.DB.get_all_themes()
                                     ))
            elif message.text == 'Мои подписки':
                await self.get_my_subscribe(
                    user_id=message.from_user.id, message=message
                    )
