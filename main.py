from aiogram.types import BotCommand
import asyncio
import logging
from bot import dp, bot
from handlers import (
myinfo_router,
picture_router,
shop_router,
start_router
)


async def mine():
    await bot.set_my_commands([
        BotCommand(command="start", description="Начать"),
        BotCommand(command="myinfo", description="Показать информацию обо мне"),
        BotCommand(command="picture", description="Показать случайную картинку"),
        BotCommand(command="shop", description="Магазин")

    ])
    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(myinfo_router)
    dp.include_router(shop_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(mine())

