import aiohttp
import asyncio


from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot("")



@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hi, I am Дима.\nJust write me something and I will repeat it!'
    await bot.reply_to(message, text)



@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)

