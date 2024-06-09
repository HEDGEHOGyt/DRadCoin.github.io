import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
API_TOKEN = "7125208923:AAFCyvT7q1jXdBWx2szIEmdSSC_kWOWlNGY"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler()
async def echo_all(message: types.Message):
    user_id = message.from_user.id
    keyboard_menu = types.InlineKeyboardMarkup()
    one = types.InlineKeyboardButton(text="ЗАПУСК", url="https://t.me/DRadCoinBot/Play")
    two = types.InlineKeyboardButton(text="КАНАЛ", url="https://t.me/DRadCoin")
    keyboard_menu.add(one)
    keyboard_menu.add(two)
    await bot.send_photo(user_id,'https://media.discordapp.net/attachments/1248735788212948995/1249175031930552440/4900_20240609043223.png?ex=66665868&is=666506e8&hm=88c1f8fa4828bbb47147ed92af03716a0953ca05767998cdb77c1b16ae4c78cc&', caption=f"Привет {message.from_user.first_name} ! Это Drad! 🌟 Ваше любимое приложение для криптовалютной торговли — все крутые монеты и токены прямо у вас в кармане!📱\n\nТеперь мы запускаем наше мини-приложение Telegram! Начните фармить очки прямо сейчас, и кто знает, какие крутые вещи вы с ними скоро поймаете! 🚀\n\nПомните: Drad — это место, где процветает рост и расцветают безграничные возможности заработать! 🌼",reply_markup=keyboard_menu)
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
