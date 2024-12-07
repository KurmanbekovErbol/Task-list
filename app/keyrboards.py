from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

buttons = [
     [KeyboardButton(text='Добавить задачу'), KeyboardButton(text='Показать задачи')],
     [KeyboardButton(text='Очистить список')]
]

keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, one_time_keyboard=True , input_field_placeholder='Выберите кнопку')


inline_button = [
     [InlineKeyboardButton(text="Подтвердить", callback_data="confirm_clear")],
     [InlineKeyboardButton(text="Отменить", callback_data="cancel_clear")]
]

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=inline_button)