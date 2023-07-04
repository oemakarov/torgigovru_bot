# ENCODING = "UTF-8"
import logging
import telebot
from logging import Handler, LogRecord
import config


class TelegramBotHandler(Handler):
    def __init__(self, token: str, chat_id: str):
        super().__init__()
        self.token = token
        self.chat_id = chat_id

    def emit(self, record: LogRecord):
        bot = telebot.TeleBot(self.token)
        bot.send_message(
            self.chat_id,
            self.format(record)
        )


def get_file_handler():
    file_handler = logging.FileHandler(config.log_filename, mode='a')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(config.log_format_file, datefmt=config.log_datefmt))
    return file_handler

def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(config.log_format_print))
    return stream_handler

def get_telegram_handler():
    telegram_handler = TelegramBotHandler(token=config.BOT_TOKEN , chat_id=config.ADMIN_USER_ID)
    telegram_handler.setLevel(logging.ERROR)
    telegram_handler.setFormatter(logging.Formatter(config.log_format_telegram))
    return telegram_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    logger.addHandler(get_telegram_handler())
    return logger
