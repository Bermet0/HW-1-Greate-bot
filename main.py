from aiogram.types import BotCommand
import asyncio
import logging
from bot import dp, bot, scheduler
from handlers import (
                      myinfo_router,
                      picture_router,
                      shop_router,
                      start_router,
                      questions_router,
                      # delayed_answer_router
)
from db.queries import init_db, create_tables, populate_tables


async def on_startup(dispatcher):
    init_db()
    create_tables()
    populate_tables()


async def mine():
    await bot.set_my_commands([
        BotCommand(command="start", description="Начать"),
        BotCommand(command="myinfo", description="Показать информацию обо мне"),
        BotCommand(command="picture", description="Показать случайную картинку"),
        BotCommand(command="shop", description="Магазин"),
        BotCommand(command="question", description="Вопрос"),
        BotCommand(command="remind", description="годовщина")
    ])

    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(myinfo_router)
    dp.include_router(shop_router)
    dp.include_router(questions_router)
    # dp.include_router(delayed_answer_router)

    dp.startup.register(on_startup)

    # scheduler.start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(mine())

