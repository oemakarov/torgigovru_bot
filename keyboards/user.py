from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


btn_user_list = InlineKeyboardButton('Перейти в список', callback_data='user_list')
btn_user_del_choice = InlineKeyboardButton('Удалить ...', callback_data='user_del_choice')
btn_user_del_one = InlineKeyboardButton('Удалить \U00002B06', callback_data='user_del_one')
btn_user_add_new_search = InlineKeyboardButton('Добавить ...', callback_data='user_add_new_search')

user_kb_list = InlineKeyboardMarkup().add(btn_user_add_new_search, btn_user_del_choice)
user_kb_list_one = InlineKeyboardMarkup().add(btn_user_list)
user_kb_del_one_search = InlineKeyboardMarkup().add(btn_user_del_one)

btn_user_fcm_cancel = InlineKeyboardButton('Отмена', callback_data='user_fsm_cancel')
user_kb_fcm_cancel = InlineKeyboardMarkup().add(btn_user_fcm_cancel)
