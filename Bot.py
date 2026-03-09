from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "8725705616:AAFOeBQ7tqeFgqKY2qc9Bj6BQDkpaa0ieKA"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):

    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            text="🌍 Բացել World Clock",
            web_app=WebAppInfo(url="https://YOUR_RAILWAY_LINK")
        )
    )

    await message.answer(
        "Բարի գալուստ World Clock Mini App ⏰",
        reply_markup=keyboard
    )


if __name__ == "__main__":
    executor.start_polling(dp)
