import abc
from aiogram import Router

from data_base.dbalchemy import DBManager
from keyboards.keyboard import Keyboards
from keyboards.inline_keyboard import InlineKeyboards


class Handler(metaclass=abc.ABCMeta):
    def __init__(self, bot):
        self.bot = bot
        self.DB = DBManager()
        self.kb = Keyboards()
        self.inline_kb = InlineKeyboards()

    @abc.abstractclassmethod
    def handle(self):
        pass
