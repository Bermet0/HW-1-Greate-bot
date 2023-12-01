from aiogram import Router, F ,types
from aiogram.filters import Command
from handlers.delayed_answer import delayed_answer_router


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
            ],
            [
                types.InlineKeyboardButton(
                    text="follow", callback_data="Подписаться"
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


# @delayed_answer_router.message(F.data == "Подписаться")
# async def follow_user(callback: types.Message):
#     user_id = str(callback.from_user.id)
#     user_name = callback.from_user.full_name
#     follow(user_id, user_name)
#     await callback.answer("вы подписались!")
