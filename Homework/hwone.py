import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import random
import os



BOT_TOKEN = '6476302799:AAFcNT6L0Ov_-FOGkzwBRe4A7b3R9d-dRv4'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Hi")

@dp.message(Command("myinfo"))
async def echo(message: types.Message):
    print(message)
    await message.answer(f" Your name is: {message.from_user.first_name}, Your id is: {message.from_user.id}")


@dp.message(Command("picture"))
async def picture(message: types.Message):
    image_path = 'images'
    images = os.listdir(image_path)
    random_image = random.choice(images)
    images_path = os.path.join(image_path, random_image)
    file = types.FSInputFile(images_path)
    await message.answer_photo(file)


async def mine():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(mine())
