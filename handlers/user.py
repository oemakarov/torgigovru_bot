from aiogram import types, Dispatcher
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

import config
from lib.sqlite import get_user_search, add_user_search, del_user_search
from lib.initialization import bot, log
from keyboards.user import user_kb_list, user_kb_del_one_search, user_kb_list_one, user_kb_fcm_cancel
from __version__ import __version__


class FSM_search_text(StatesGroup):
    search_text = State()


async def command_start(message: types.Message):
    message_text = f'''<b>torgigovru_bot</b>
Поисковый бот по ГИС Торги (torgi.gov.ru), присылает извещения с сайта полученные <b>ПОСЛЕ</b> настройки поиска. 

Возможности:
<code>@номер - номер региона
слово - отдельно слово не в составе другого, отделено пробелами или знаками препинания
*часть* - часть слова 
+ - объединяет составляюшие одного запроса</code>

Примеры:
\U000025AB <u>@92</u> - поиск всех торгов в регионе 92 - Севастополь
\U000025AB <u>@91+симферополь</u> - регион Крым, город Симферополь
\U000025AB <u>@23+*парк*</u> - Краснодарский край + парк/парковая/парковка/паркомат
\U000025AB <u>@50+*авто*+*невск*</u> - Московская область + автомобиль/автоматические ворота + ул Невская/пр. Невский
\U000025AB <u>автобус+паз</u> - все автобусы ПАЗ страны, т.к. без региона

Самый частый вариант - @регион+город - все торги вашего города

<code>v{__version__}</code>
'''
    await bot.send_message(message.from_user.id, message_text, parse_mode=types.ParseMode.HTML)
    await show_list(message)


async def del_choice(call: CallbackQuery):
    search_list = await get_user_search(call.message.chat.id)
    if search_list:
        for search in search_list:
            await bot.send_message(call.message.chat.id, search, reply_markup=user_kb_del_one_search)
    else:
        await show_list(call.message)


async def del_one(call: CallbackQuery):
    log.info(f'user_id = {call.message.chat.id} - del {call.message.text}')
    await del_user_search(call.message.chat.id, call.message.text)
    await call.message.edit_text(f'\U0000274C <s>{call.message.text}</s>',
                                 parse_mode=types.ParseMode.HTML,
                                 reply_markup=user_kb_list_one)


async def show_list_callback(call: CallbackQuery):
    await show_list(call.message)


async def show_list(message: types.Message):
    log.info(f'user_id = {message.chat.id} ({message.chat.username} - {message.chat.first_name} {message.chat.last_name})')
    search_list = await get_user_search(message.chat.id)
    message_text = '<b>Список поисковых запросов:</b>\n'
    if search_list:
        message_text += '\n'.join([f'\U000025AB {s}'for s in search_list])
    else:
        message_text += '[ПУСТО]'
    message_text += '\n\nНе знаешь что писать - жми /start'
    await message.answer(message_text, parse_mode=types.ParseMode.HTML, reply_markup=user_kb_list)


async def unknown_message(message: types.Message):
    await command_start(message)


async def add_new_search(call: CallbackQuery):
    await call.message.answer('\U00002753Введите поисковый запрос ... ', reply_markup=user_kb_fcm_cancel)
    await FSM_search_text.search_text.set()


async def process_new_search_text(message: types.Message, state: FSMContext):
    log.info(f'user_id = {message.chat.id} - add_user_search - {message.text}')
    await add_user_search(message.chat.id,
                          message.text,
                          message.chat.username,
                          message.chat.first_name,
                          message.chat.last_name)
    await state.finish()
    await show_list(message)
    message_text = f'\U000025AB <code>torgigovru | {message.chat.id} |' \
                   f'{" " + message.chat.username if message.chat.username else ""}' \
                   f'{" " + message.chat.first_name if message.chat.first_name else ""}' \
                   f'{" " + message.chat.last_name if message.chat.last_name else ""}\n' \
                   f'{message.text}</code>'
    await admin_message(message_text, parse_mode=types.ParseMode.HTML)


async def fcm_cancel(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await show_list(call.message)


async def admin_message(message_text: str, parse_mode: types.ParseMode = None):
    await bot.send_message(config.admin_user_id, message_text, parse_mode=parse_mode, disable_notification=True)


def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(process_new_search_text, state=FSM_search_text.search_text)
    dp.register_callback_query_handler(show_list_callback, text='user_list')
    dp.register_callback_query_handler(del_choice, text='user_del_choice')
    dp.register_callback_query_handler(del_one, text='user_del_one')
    dp.register_callback_query_handler(add_new_search, text='user_add_new_search')
    dp.register_callback_query_handler(fcm_cancel, text='user_fsm_cancel', state='*')
    dp.register_message_handler(unknown_message)
