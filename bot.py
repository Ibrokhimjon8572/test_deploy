
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

# answers = [
#     ("6", "7", "8"),
#     ("0", "9", "-1"),
# ]

# def makekeyboard(question_id: str):
#     markup = types.InlineKeyboardMarkup()
#     for answer_id, answer in enumerate(answers[question_id]):
#         markup.add(types.InlineKeyboardButton(text=answer, callback_data=f"{question_id}_{answer_id}"))
#     return markup

# @bot.message_handler(commands=['test'])
# def handle_test(msg: types.Message):
#     if msg.from_user.id != msg.chat.id:
#         return 
#     bot.send_message(chat_id=msg.chat.id,
#                     text="2 + 4 = ?",
#                     reply_markup=makekeyboard(0),
#                     parse_mode='HTML')

# @bot.callback_query_handler(func=lambda call:True)
# def handle_answer(cb: types.CallbackQuery):
#     question_id, answer_id = cb.data.split("_")
#     bot.edit_message_text("4+5 = ?")
#     bot.edit_message_reply_markup(makekeyboard(1))

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