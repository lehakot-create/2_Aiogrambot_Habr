from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

from models.themes import Themes


class NumbersCallbackFactory(CallbackData, prefix='fabnum'):
    id: int


class InlineKeyboards:
    def __init__(self):
        self.markup = None

    def inline_list_themes(self, themes: list[Themes]):
        self.markup = InlineKeyboardBuilder()
        for theme in themes[:5]:
            self.markup.button(
                text=theme.title,
                callback_data=NumbersCallbackFactory(id=theme.id)
            )
        self.markup.adjust(1)
        return self.markup.as_markup()
