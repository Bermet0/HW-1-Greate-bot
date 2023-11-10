import asyncio
import os
import random
from pathlib import Path

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging



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
# async def send_random_picture(message: types.Message):
     # folder_path = 'images/'
    # images = os.listdir(folder_path)
    # random_image = random.choice(images)
    # image_path = os.path.join(folder_path, random_image)
    # photo = types.InputFile(image_path)
    # await message.answer_photo(photo)
async def picture(message: types.Message):
    image_path = Path("images/")
    images = list(image_path.iterdir())
    random_image = random.choice(images)

    with random_image.open('rb') as photo:
        await message.answer_photo(photo)


    # file = types.FSInputFile('images/')
    # await message.answer_photo(
    #     photo=file
    # )
    # bot.send_photo(file, 'photo:')


async def mine():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(mine())
