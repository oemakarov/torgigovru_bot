# -*- coding: utf-8 -*-

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# import logging
import lib.app_logger as app_logger

import config

log = app_logger.get_logger('torgigovru_bot')
storage = MemoryStorage()
bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)
