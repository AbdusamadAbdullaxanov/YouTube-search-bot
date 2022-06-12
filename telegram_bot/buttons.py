from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

randomize = KeyboardButton("Random videos")
single_button = KeyboardButton("Single random video")
random_button = ReplyKeyboardMarkup(resize_keyboard=True).add(randomize, single_button)
