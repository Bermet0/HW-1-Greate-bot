from aiogram import Router, F, types
from aiogram.filters import Command
from db.queries import get_products
from db.queries import get_product_by_category_id


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
    heroes = get_product_by_category_id(1)
    await message.answer(f"Герои в нашем магазине:")
    for hero in heroes:
        await message.answer(f"{hero[1]}\nPrice: {hero[2]}", reply_markup=kb)


@shop_router.message(F.text == "Скины")
async def show_skin(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    skins = get_product_by_category_id(2)
    await message.answer(f"Скины в нашем магазине:")
    for skin in skins:
        await message.answer(f"{skin[1]}\nPrice: {skin[2]}", reply_markup=kb)
