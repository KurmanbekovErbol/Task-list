import sqlite3
from app.keyrboards import *

connect= sqlite3.connect("Task_list.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
telegram_user INTEGER UNIQUE,
name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
telegram_user INT,
task TEXT
)
""")
connect.commit()

def register(telegram_user, name):
    cursor.execute(f"SELECT telegram_user FROM users WHERE telegram_user = ({telegram_user})")
    users = cursor.fetchall()
    if users:
        pass
    else:
        cursor.execute(f"INSERT INTO users (telegram_user, name) VALUES ({telegram_user}, '{name}')")
        connect.commit()

def add_task(telegram_user, task):
        cursor.execute("SELECT telegram_user FROM users WHERE telegram_user = ?", (telegram_user,))
        user_id = cursor.fetchone()
        if user_id:
            cursor.execute("INSERT INTO tasks (telegram_user, task) VALUES (?, ?)", (telegram_user, task))
            connect.commit()
        else:
             pass

# def get_tasks(telegram_user):
#         cursor.execute(f"SELECT task FROM tasks WHERE telegram_user = ({telegram_user})")
#         return cursor.fetchall()

def get_tasks(telegram_user):
    directions = cursor.execute(f"SELECT task FROM tasks WHERE telegram_user = ({telegram_user})")
    directions = cursor.fetchall()
    list_direction = []
    for i in directions:
        list_direction.append(i[0])
    return list_direction


def delete_all_tasks(telegram_user):
        cursor.execute(f"DELETE FROM tasks WHERE telegram_user = ({telegram_user})")
        connect.commit()

async def tasks_buttons(telegram_user):
    tasks = get_tasks(telegram_user)
    markup = InlineKeyboardBuilder()
    for task in tasks:
        markup.add(InlineKeyboardButton(text=task, callback_data=f"task_{task}"))
    return markup.adjust(1).as_markup()
