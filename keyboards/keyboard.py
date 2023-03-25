from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class Keyboards:
    def __init__(self):
        self.markup = None

    def main_kb(self) -> ReplyKeyboardMarkup:
        self.markup = ReplyKeyboardBuilder()
        self.markup.add(KeyboardButton(text='Получить новости'))
        self.markup.add(KeyboardButton(text='Все темы'))
        self.markup.add(KeyboardButton(text='Мои подписки'))
        self.markup.adjust(3)
        return self.markup.as_markup(resize_keyboard=True)
