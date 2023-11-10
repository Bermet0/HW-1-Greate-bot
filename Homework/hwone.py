import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging
import os
import random



BOT_TOKEN = '6476302799:AAFcNT6L0Ov_-FOGkzwBRe4A7b3R9d-dRv4'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Hi")

@dp.message(Command("myinfo"))
async def myinfo(messege: types.Message):
    await messege.answer(f'User ID:123 \n'
                         f'User first_name:Molly \n'
                         f'User username: Moly123')


@dp.message(Command("picture"))
async def picture(message: types.Message):
    file = types.FSInputFile("images/")
    images = os.listdir(file)
    random_im = random.choice(images)
    await message.answer_photo(
        photo=random_im,
        caption="Кадита"
    )



async def hwone():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(hwone())
