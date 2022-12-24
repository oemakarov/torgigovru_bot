from aiogram import types, Dispatcher
from initialization import bot

async def command_admin(message: types.Message):
    await bot.send_message(message.from_user.id, 'hello admin, watsup')


def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(command_admin, commands=['admin'])
