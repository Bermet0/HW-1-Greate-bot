from aiogram import Router, types
from aiogram.filters import Command
import os
import random


picture_router = Router()


@picture_router.message(Command("picture"))
async def picture(message: types.Message):
    image_path = 'images'
    images = os.listdir(image_path)
    random_image = random.choice(images)
    images_path = os.path.join(image_path, random_image)
    file = types.FSInputFile(images_path)
    await message.answer_photo(file)
