from aiogram import Router, F , types
from aiogram.filters import Command

shop_router = Router()

diamond = 0

@shop_router.message(Command("shop"))
async def shop(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Мои алмазы")
            ],
            [
                types.KeyboardButton(text="50 алмазов"),
                types.KeyboardButton(text="100 алмазов"),
                types.KeyboardButton(text="150 алмазов"),
            ]
        ],
        resize_keyboard=True
    )

    await message.answer("Выберите сумму для покупки:", reply_markup=kb)


@shop_router.message(F.text == "Мои алмазы")
async def show_books(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer(f"На вашем счете: {diamond}", reply_markup=kb)


@shop_router.message(F.text == "50 алмазов")
async def show_books(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer(f"На вашем счете: {diamond + 50}", reply_markup=kb)


@shop_router.message(F.text == "100 алмазов")
async def show_books(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer(f"На вашем счете: {diamond + 100}", reply_markup=kb)


@shop_router.message(F.text == "150 алмазов")
async def show_books(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer(f"На вашем счете: {diamond + 150}", reply_markup=kb)
