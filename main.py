import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config_data.config import load_config
from handlers import start, survey, quiz, echo

logging.basicConfig(level=logging.INFO)

config = load_config()

bot = Bot(token=config.bot_token)
dp = Dispatcher(storage=MemoryStorage())

# Регистрируем все обработчики
logging.info("Подключение обработчиков...")
dp.include_router(start.router)
dp.include_router(survey.router)
dp.include_router(quiz.router)
dp.include_router(echo.router)
logging.info("Обработчики подключены успешно")

if __name__ == "__main__":
    dp.run_polling(bot)
