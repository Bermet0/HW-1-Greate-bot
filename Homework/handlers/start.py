from aiogram import Router, F ,types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):

    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Наш discord", url="https://discord.com/invite/mlbbcis"
                ),
                types.InlineKeyboardButton(
                    text="Наш youtube", url="https://www.youtube.com/@mlbbcis"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="О нас", callback_data="about"
                )
            ]
        ]
    )

    await message.answer(
        f"Hi, @{message.from_user.username}",
        reply_markup=kb
    )


@start_router.callback_query(F.data == "about")
async def about_us(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Мы многопользовательская командная видеоигра для мобильных устройств")
