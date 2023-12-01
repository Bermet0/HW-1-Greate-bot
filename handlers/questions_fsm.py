from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from db.queries import save_questionaire


questions_router = Router()


class Questionaire(StatesGroup):
    name = State()
    age = State()
    gender = State()
    meet_play = State()


@questions_router.message(Command("stop"))
@questions_router.message(F.text == "stop")
async def stop_questions(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Вопросы прерваны")


@questions_router.message(Command("question"))
async def start_questions(message: types.Message, state: FSMContext):
    await state.set_state(Questionaire.name)
    await message.answer("Для выхода введите 'stop'")
    await message.answer("Как вас зовут?")


@questions_router.message(F.text, Questionaire.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Questionaire.age)
    await message.answer("Ваш возраст?")


@questions_router.message(F.text, Questionaire.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text.strip()
    if not age.isdigit():
        await message.answer("Возраст состоит чисел")
    elif int(age) < 10 or int(age) > 100:
        await message.answer("Возраст должен быть от 10 до 100")
    else:
        await state.update_data(age=int(age))

        kb = types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton(text="Муж"),
                    types.KeyboardButton(text="Жен")
                ]
            ],
        resize_keyboard = True
        )
        await state.set_state(Questionaire.gender)
        await message.answer("Ваш пол?", reply_markup=kb)


@questions_router.message(F.text, Questionaire.gender)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(Questionaire.meet_play)
    await message.answer("какой год вы играете в нашу игру?")


@questions_router.message(F.text, Questionaire.meet_play)
async def process_meet_play(message: types.Message, state: FSMContext):
    meet = message.text.strip()
    if not meet.isdigit():
        await message.answer("Введите ответ в числах(год)")
    elif int(meet) < 1 or int(meet) > 8:
        await message.answer("Наша игра вышла в 2016 г")
    else:
        await state.update_data(meet_play=int(meet))

    data = await state.get_data()
    save_questionaire(data)
    # print(data)
    await state.clear()
    await message.answer("Спасибо за ваши ответы!")
