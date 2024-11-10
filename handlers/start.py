from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from lexicon.lexicon_ru import LEXICON

router = Router()

quiz_button = KeyboardButton(text="Пройти викторину")
survey_button = KeyboardButton(text="Пройти опрос")

keyboard = ReplyKeyboardMarkup(
    keyboard=[[quiz_button, survey_button]],
    resize_keyboard=True
)

@router.message(Command(commands=["start"]))
async def start_command(message: Message):
    await message.answer(LEXICON["/start"], reply_markup=keyboard)

@router.message(Command("info"))
async def info_command(message: Message):
    await message.answer(LEXICON["/info"], reply_markup=keyboard)
