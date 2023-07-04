from pathlib import Path
import config_secret

# BOT_TOKEN = config_prod_test.BOT_TOKEN
BOT_TOKEN = config_secret.BOT_TOKEN  # @torgigovru_bot
ADMIN_USER_ID = config_secret.ADMIN_USER_ID

sqlite_db_filename = Path('data', 'user_data.db')

log_logger_name = 'torgigovru_bot'
log_filename = Path('log', 'run.log')
log_format = '[%(asctime)s.%(msecs)03d]:%(lineno)d [%(levelname)s] (%(filename)s).%(funcName)s - %(message)s'
log_format_file = '[%(asctime)s.%(msecs)03d] [%(levelname)s] %(message)s'
log_format_print = '[%(asctime)s] [%(levelname)s] %(message)s'
log_format_telegram = '[%(asctime)s.%(msecs)03d] [%(levelname)s] %(message)s'
log_datefmt = '%Y-%m-%d %H:%M:%S'
# log_datefmt = '%H:%M:%S'

