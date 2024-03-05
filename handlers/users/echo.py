import types
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup,WebAppInfo
from aiogram.dispatcher.filters import Text

from loader import dp,bot

from aiogram import types



@dp.message_handler(text="Game")
async def bot_start(message: types.Message):
    await bot.send_game(chat_id=message.chat.id,game_short_name="gamemath")

@dp.callback_query_handler(lambda c: c.game_short_name == "gamemath")
async def process_game(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Let's play a game! Click the link below to start.", reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="Play Game", web_app=WebAppInfo(url=f"https://aquamarine-manatee-c25dc5.netlify.app/"))]
    ]))

