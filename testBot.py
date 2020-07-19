from telebot import types
import telebot
from service import VovaPunishService
import os, re


TOKEN = '902148830:AAGUIUgNQPfJzul8WnC6INB82KtbIKQlgqE'
JOBLIST = 'https://aoverinapp.herokuapp.com/joblists'
USERS = 'https://aoverinapp.herokuapp.com/users'
# bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=["start"])
# def inline(message):
#     key = types.InlineKeyboardMarkup()
#     but_1 = types.InlineKeyboardButton(text="NumberOne", callback_data="NumberOne")
#     but_2 = types.InlineKeyboardButton(text="NumberTwoNumber4Number4Number4Number4Number4Number4", callback_data="NumberTwo")
#     but_3 = types.InlineKeyboardButton(text="NumberTree", callback_data="NumberTree")
#     but_4 = types.InlineKeyboardButton(text="Number4Number4Number4Number4Number4Number4", callback_data="Number4")
#     key.add(but_1, but_2, but_3, but_4)
#     bot.send_message(message.chat.id, "ВЫБЕРИТЕ КНОПКУ", reply_markup=key)
#
# @bot.callback_query_handler(func=lambda c:True)
# def inlin(c):
#     if c.data == 'NumberOne':
#         bot.send_message(c.message.chat.id, 'Это кнопка 1')
#     if c.data == 'NumberTwo':
#         bot.send_message(c.message.chat.id, 'Это кнопка 2')
#     if c.data == 'NumberTree':
#         bot.send_message(c.message.chat.id, 'Это кнопка 3')
#     if c.data == 'Number4':
#         bot.send_message(c.message.chat.id, 'Это кнопка 4')




#    elif c.data == 'NumberTwo':
#        bot.send_message(c.message.chat.id, 'Это мазафака, кнопка 2')




# bot.polling()

v = VovaPunishService(None)

v.add_stat_punish("Бла бла")
v.add_stat_punish("Бла бла")
v.add_stat_punish("Бла")
print(v.get_stat_punish())
