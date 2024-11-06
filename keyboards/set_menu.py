from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_main_menu() -> ReplyKeyboardMarkup:
    kb_builder = ReplyKeyboardBuilder()
    kb_builder.add(KeyboardButton(text="Пройти опрос"))
    kb_builder.add(KeyboardButton(text="Пройти викторину"))
    return kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
