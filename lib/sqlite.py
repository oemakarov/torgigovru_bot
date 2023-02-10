import datetime
import sqlite3 as sq

from lib.initialization import log
import config


def sql_start():
    global base, cur
    base = sq.connect(config.sqlite_db_filename)
    cur = base.cursor()
    if base:
        log.info('data base - connected - OK')
    base.execute('''CREATE TABLE IF NOT EXISTS 
                        users(
                            id INTEGER PRIMARY KEY, 
                            add_datetime TEXT, 
                            user_id TEXT, 
                            search TEXT,
                            send_link INTEGER DEFAULT 0,
                            username TEXT, 
                            user_firstname TEXT, 
                            user_lastname TEXT, 
                            send_datetime TEXT, 
                            send_times INTEGER DEFAULT 0
                            )''')
    base.commit()


async def add_user_search(user_id: str,
                          search: str,
                          username: str,
                          user_firstname: str,
                          user_lastname: str):
    base.execute('''INSERT INTO users (
                            add_datetime,
                            user_id,
                            search,
                            username,
                            user_firstname,
                            user_lastname)
                    VALUES (?, ?, ?, ?, ?, ?)''',
                 (str(datetime.datetime.now()),
                  user_id,
                  search,
                  username,
                  user_firstname,
                  user_lastname))
    base.commit()


async def get_user_search(user_id: str) -> list:
    rows = cur.execute('SELECT search FROM users WHERE user_id=?', (str(user_id), )).fetchall()
    return [r[0] for r in rows]


async def del_user_search(user_id: int, search: str):
    base.execute('''DELETE FROM users 
                        WHERE user_id=? 
                        AND 
                        search=?''', (user_id, search))
    base.commit()



# def add_field():
#     cur.execute("ALTER TABLE users ADD COLUMN send_link 'INTEGER DEFAULT 0'")




# async def del_all_user_search(user_id: int):
#     base.execute('''DELETE FROM users 
#                         WHERE user_id=?''', (user_id, ))
#     base.commit()
