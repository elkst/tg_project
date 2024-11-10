from aiogram import Router, F
from aiogram.types import Message
from keyboards.set_menu import get_main_menu
from database.survey_questions import survey_questions
from database.user_data import get_user_data, clear_user_data

router = Router()

@router.message(F.text == "Пройти опрос")
async def start_survey(message: Message):
    user_data = get_user_data(message.from_user.id)
    user_data["survey_step"] = 0
    user_data["survey_answers"] = []
    await ask_survey_question(message)

async def ask_survey_question(message: Message):
    user_data = get_user_data(message.from_user.id)
    step = user_data["survey_step"]
    question = survey_questions[step]
    await message.answer(question, reply_markup=None)

@router.message(lambda message: "survey_step" in get_user_data(message.from_user.id))
async def handle_survey_answer(message: Message):
    user_data = get_user_data(message.from_user.id)
    step = user_data["survey_step"]
    user_data["survey_answers"].append(message.text)

    if step + 1 < len(survey_questions):
        user_data["survey_step"] += 1
        await ask_survey_question(message)
    else:
        results = "\n".join(f"{q}: {a}" for q, a in zip(survey_questions, user_data["survey_answers"]))
        await message.answer(f"Спасибо за участие в опросе!\nВаши ответы:\n{results}", reply_markup=get_main_menu())
        clear_user_data(message.from_user.id)
