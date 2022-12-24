from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

btn_send_message_to_users = InlineKeyboardButton('Отправить сообщение всем пользователям',
                                                 callback_data='admin_send_message_to_users')
btn_show_users = InlineKeyboardButton('Показать всех пользователей',
                                                 callback_data='admin_show_users')



btn_user_add = InlineKeyboardButton('Добавить', callback_data='add')

user_kb_new_word = InlineKeyboardMarkup().add(btn_user_add, btn_user_list)
# user_kb_new_word = user_kb_new_word


