from aiogram.utils.exceptions import BotBlocked, MessageNotModified
from aiogram import types, Dispatcher


async def error_bot_blocked_handler(update: types.Update, exception: BotBlocked):
    print('не могу отправить сообщение - нас заблокировали')
    print(f'{update = }')
    print(f'{exception = }')
    return True

# async def error_bot_blocked_handler(update: types.Update, exception: MessageNotModified):
#     print('не могу отправить сообщение - нас заблокировали')
#     print(f'{update = }')
#     print(f'{exception = }')
#     return True


def register_handlers_error(dp: Dispatcher):
    dp.register_errors_handler(error_bot_blocked_handler, exception=BotBlocked)
    # dp.register_errors_handler(error_bot_blocked_handler, exception=MessageNotModified)