from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class Keyboards:
    def __init__(self):
        self.markup = None

    def get_yes_no_kb(self) -> ReplyKeyboardMarkup:
        self.markup = ReplyKeyboardBuilder()
        self.markup.add(KeyboardButton(text="Да"))
        self.markup.add(KeyboardButton(text="Нет"))
        self.markup.adjust(2)
        return self.markup.as_markup(resize_keyboard=True)
