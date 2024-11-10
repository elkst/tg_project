from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from database.user_data import get_user_data

router = Router()

@router.message(Command("echo"))
async def toggle_echo_mode(message: Message):
    user_id = message.from_user.id
    user_data = get_user_data(user_id)

    user_data["echo_mode"] = not user_data.get("echo_mode", False)
    status = "включен" if user_data["echo_mode"] else "выключен"
    await message.answer(f"Режим эхо {status}.")

@router.message(lambda message: message.content_type == ContentType.TEXT)
async def echo_text_message(message: Message):
    user_id = message.from_user.id
    user_data = get_user_data(user_id)

    if user_data.get("echo_mode", False):
        await message.answer(message.text)

# Эхо-ответ для GIF (анимаций)
@router.message(lambda message: message.content_type == ContentType.ANIMATION)
async def echo_gif_message(message: Message):
    user_id = message.from_user.id
    user_data = get_user_data(user_id)

    if user_data.get("echo_mode", False):
        await message.answer_animation(message.animation.file_id)

# Эхо-ответ для геолокации
@router.message(lambda message: message.content_type == ContentType.LOCATION)
async def echo_location_message(message: Message):
    user_id = message.from_user.id
    user_data = get_user_data(user_id)

    if user_data.get("echo_mode", False):
        latitude = message.location.latitude
        longitude = message.location.longitude
        await message.answer_location(latitude=latitude, longitude=longitude)

# Эхо-ответ для документов
@router.message(lambda message: message.content_type == ContentType.DOCUMENT)
async def echo_document_message(message: Message):
    user_id = message.from_user.id
    user_data = get_user_data(user_id)

    if user_data.get("echo_mode", False):
        await message.answer_document(message.document.file_id)

# Эхо-ответ для фото
@router.message(lambda message: message.content_type == ContentType.PHOTO)
async def echo_photo_message(message: Message):
    user_id = message.from_user.id
    user_data = get_user_data(user_id)

    if user_data.get("echo_mode", False):
        await message.answer_photo(message.photo[-1].file_id)

# Эхо-ответ для стикеров
@router.message(lambda message: message.content_type == ContentType.STICKER)
async def echo_sticker_message(message: Message):
    user_id = message.from_user.id
    user_data = get_user_data(user_id)

    if user_data.get("echo_mode", False):
        await message.answer_sticker(message.sticker.file_id)

# Эхо-ответ для видео
@router.message(lambda message: message.content_type == ContentType.VIDEO)
async def echo_video_message(message: Message):
    user_id = message.from_user.id
    user_data = get_user_data(user_id)

    if user_data.get("echo_mode", False):
        await message.answer_video(message.video.file_id)

# Эхо-ответ для аудио
@router.message(lambda message: message.content_type == ContentType.AUDIO)
async def echo_audio_message(message: Message):
    user_id = message.from_user.id
    user_data = get_user_data(user_id)

    if user_data.get("echo_mode", False):
        await message.answer_audio(message.audio.file_id)

# Эхо-ответ для голосовых сообщений
@router.message(lambda message: message.content_type == ContentType.VOICE)
async def echo_voice_message(message: Message):
    user_id = message.from_user.id
    user_data = get_user_data(user_id)

    if user_data.get("echo_mode", False):
        await message.answer_voice(message.voice.file_id)
