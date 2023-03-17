from aiogram import Router
from aiogram.filters import Command
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove

# from keyboards.for_questions import get_yes_no_kb
from handlers.handler import Handler

# router = Router()  # [1]


class HandlerCommands(Handler):
    def __init__(self, bot):
        super().__init__(bot)
        self.router = Router()

    def handle(self):
        @self.router.message(Command('start'))
        async def cmd_start(message: Message):
            await message.answer(f'Welcome {message.from_user.username}!!!',
                                 reply_markup=self.kb.get_yes_no_kb())
            await message.answer(f'Welcome {message.from_user.first_name}!!!',
                                 reply_markup=self.kb.get_yes_no_kb())
            await message.answer(f'Welcome {message.from_user.full_name}!!!',
                                 reply_markup=self.kb.get_yes_no_kb())
            # self.DB.add_user(user_id=message.from_user.id,
            #                  username=message.from_user.username,
            #                  first_name=message.from_user.first_name,
            #                  full_name=message.from_user.full_name)

# @router.message(Command("start"))  # [2]
# async def cmd_start(message: Message):
#     await message.answer(
#         "Вы довольны своей работой?",
#         reply_markup=get_yes_no_kb()
#     )


# @router.message(Text(text="да", ignore_case=True))
# async def answer_yes(message: Message):
#     await message.answer(
#         "Это здорово!",
#         reply_markup=ReplyKeyboardRemove()
#     )


# @router.message(Text(text="нет", ignore_case=True))
# async def answer_no(message: Message):
#     await message.answer(
#         "Жаль...",
#         reply_markup=ReplyKeyboardRemove()
#     )
