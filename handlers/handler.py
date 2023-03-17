import abc
from aiogram import Router

from data_base.dbalchemy import DBManager
from keyboards.for_questions import Keyboards


class Handler(metaclass=abc.ABCMeta):
    def __init__(self, bot):
        self.bot = bot
        self.DB = DBManager()
        # self.router = Router()
        self.kb = Keyboards()

    @abc.abstractclassmethod
    def handle(self):
        pass
