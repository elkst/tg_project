from aiogram import Router, F
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keyboards.set_menu import get_main_menu
from database.quiz_questions import quiz_questions
from database.user_data import get_user_data, clear_user_data

router = Router()

@router.message(F.text == "Пройти викторину")
async def start_quiz(message: Message):
    user_data = get_user_data(message.from_user.id)
    user_data["quiz_step"] = 0
    user_data["correct_answers"] = 0
    await ask_quiz_question(message)

async def ask_quiz_question(message: Message):
    user_data = get_user_data(message.from_user.id)
    step = user_data["quiz_step"]
    question, options, _ = quiz_questions[step]

    kb_builder = ReplyKeyboardBuilder()
    for option in options:
        kb_builder.add(KeyboardButton(text=option))
    keyboard = kb_builder.as_markup(resize_keyboard=True)
    await message.answer(question, reply_markup=keyboard)

@router.message(lambda message: "quiz_step" in get_user_data(message.from_user.id))
async def handle_quiz_answer(message: Message):
    user_data = get_user_data(message.from_user.id)
    step = user_data["quiz_step"]
    _, _, correct_answer = quiz_questions[step]

    if message.text == correct_answer:
        user_data["correct_answers"] += 1
        await message.answer("Правильно!")
    else:
        await message.answer(f"Неправильно. Правильный ответ: {correct_answer}")

    if step + 1 < len(quiz_questions):
        user_data["quiz_step"] += 1
        await ask_quiz_question(message)
    else:
        total_questions = len(quiz_questions)
        correct_answers = user_data["correct_answers"]
        await message.answer(f"Викторина окончена! Вы ответили правильно на {correct_answers} из {total_questions} вопросов.", reply_markup=get_main_menu())
        clear_user_data(message.from_user.id)  # Clear data after completion
