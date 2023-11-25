from aiogram import Router, F, types
from aiogram.filters import Command
from db.queries import get_products


shop_router = Router()


@shop_router.message(Command("shop"))
async def shop(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Герои"),
                types.KeyboardButton(text="Скины")
            ]
        ],
        resize_keyboard=True
    )

    await message.answer("Выберите категорию:", reply_markup=kb)

@shop_router.message(F.text == "Герои")
async def show_heroes(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    heroes = get_products()
    await message.answer(f"Герои в нашем магазине:", reply_markup=kb)
    for hero in heroes:
        await message.answer(f"{hero[1]}\nPrice: {hero[2]}")
