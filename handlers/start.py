from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.set_menu import get_main_menu

router = Router()

@router.message(CommandStart())
async def start_command_handler(message: Message):
    await message.answer("Привет! Выберите, что хотите сделать:", reply_markup=get_main_menu())
