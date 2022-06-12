from aiogram import Bot, Dispatcher, executor, types
import logging
from database import Function
from config import TOKEN
from buttons import *
from youtube_search import YoutubeSearch

bot = Bot(TOKEN)
dispatcher = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dispatcher.message_handler(commands=["start"])
async def start(message: types.Message):
    if message.from_user.username == "Asuna774":
        await message.reply("Shoxista opa yoqsa /like yoqmasa /dislike ni bosing: Baho bering ❤❤❤",
                            reply_markup=random_button)
    elif message.from_user.username == "azizbekrahimjonov571":
        await message.reply("Domla qalay chiqibdi, botga baho bering /like vs /dislike")
    else:
        await message.reply(
            f"Hello {message.from_user.first_name}! This bot really helps you to search videos on YouTube! This is super easy!",
            reply_markup=random_button)


@dispatcher.message_handler()
async def search(message: types.Message):
    fun = Function()
    if message.text == "Single random video":
        await message.reply(f"👉 https://youtube.com/watch?v={fun.retrieve_link()}", reply_markup=random_button)
    elif message.text == "Whole bunches of random videos":
        print(True)
        for i in range(1, 8):
            await message.reply(f"👉 https://youtube.com/watch?v={fun.retrieve_link()}", reply_markup=random_button)
    else:
        response = YoutubeSearch(message.text, max_results=20).to_dict()
        for i in range(1, 20):
            video = response[i - 1]
            fun.insert_id(video_id=video.get("id"), username=message.from_user.username, search_title=message.text)
            await message.reply(
                f"👉 https://youtube.com/watch?v={video.get('id')}\n👉 {video.get('title')}\n👉 duration: {video.get('duration')}",
                reply_markup=random_button)


@dispatcher.message_handler(commands=["like", "dislike"])
async def feedback(message: types.Message):
    await message.answer("Thank you a lot for feedback!")


executor.start_polling(dispatcher)
