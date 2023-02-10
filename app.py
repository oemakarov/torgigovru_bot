# -*- coding: utf-8 -*-

from aiogram.utils import executor

from handlers import user, admin, errors
from lib.initialization import dp, log
from lib.sqlite import sql_start
from __version__ import __version__

admin.register_handlers_admin(dp)
user.register_handlers_user(dp)
errors.register_handlers_error(dp)


async def on_startup(_):
    log.error(f'----- BOT START v{__version__}')
    sql_start()


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
