
import os
from dotenv import load_dotenv
import telebot
from telebot import types

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
GROUP_ID = os.getenv('GROUP_ID')
# print(BOT_TOKEN)
# print()

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(msg: types.Message):
    if msg.from_user.id != msg.chat.id:
        return
    print(msg.chat.id)
    bot.send_message(msg.chat.id, "Vazifalarni ushbu bot orqali yuborishingiz mumkun!!..")
    bot.send_message(msg.chat.id, ".zip da ism-familya, guruh, qaysi kun vazifasi yoritilishi kerak")
    file = open("example.zip", "rb")
    bot.send_document(msg.chat.id, file, caption="Ism: Mamajonov\nFamilya: Ibrohimjon,\nGuruh: N17,\nSana: 12.07.2023")
    

@bot.message_handler(content_types=["document"])
def echo_all(message: types.Message):
    bot.forward_message(GROUP_ID, message.chat.id, message.id)
    bot.send_message(message.chat.id, "Tekshirish uchun file jo'natildi!!..")

bot.infinity_polling()