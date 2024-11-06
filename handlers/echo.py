from aiogram import Router, F
from aiogram.types import Message, ContentType

router = Router()

@router.message(F.content_type == ContentType.TEXT)
async def echo_text(message: Message):
    await message.reply(f"Эхо: {message.text}")

@router.message(F.content_type == ContentType.PHOTO)
async def echo_photo(message: Message):
    await message.reply_photo(message.photo[-1].file_id)

@router.message(F.content_type == ContentType.STICKER)
async def echo_sticker(message: Message):
    await message.reply_sticker(message.sticker.file_id)

@router.message(F.content_type == ContentType.VIDEO)
async def echo_video(message: Message):
    await message.reply_video(message.video.file_id)

@router.message(F.content_type == ContentType.AUDIO)
async def echo_audio(message: Message):
    await message.reply_audio(message.audio.file_id)

@router.message()
async def echo_all_other(message: Message):
    await message.reply("Я пока не знаю, как ответить на это сообщение.")
