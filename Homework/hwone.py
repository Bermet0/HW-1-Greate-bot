import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import random
import os
from pathlib import Path
from random import choice

ml = []

p = Path("images/")
for c in p.iterdir():
    ml.append(c)
    print(c)

choice(ml)

BOT_TOKEN = '6476302799:AAFcNT6L0Ov_-FOGkzwBRe4A7b3R9d-dRv4'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Hi")

@dp.message(Command("myinfo"))
async def echo(message: types.Message):
    print(message)
        # print(message.text)
        # await message.answer("hi")
    await message.answer(f" Your name is: {message.from_user.first_name}, Your id is: {message.from_user.id}")

@dp.message(Command("picture"))
async def picture(message: types.Message):
    file = types.FSInputFile(choice(ml))
    await message.answer_photo(
        photo=file,
    )

# @dp.message(Command("picture"))
# async def picture(message: types.Message):
#     image = random.choice(os.listdir(path=".\images"))
#     images = types.FSInputFile(f'./images/{image}')
#     await message.reply_photo(photo=images)



async def mine():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(mine())
