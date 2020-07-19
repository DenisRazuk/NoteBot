import telebot
import os
import random
from datetime import datetime as dt
from DBApi import VovaPunishDAO
import service

dbname = os.environ.get('dbname')
user = os.environ.get('user')
password = os.environ.get('password')
host = os.environ.get('host')
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)
vovaDAO = VovaPunishDAO(dbname, user, password, host)
vovaSer = service.VovaPunishService(vovaDAO)


@bot.message_handler(commands=['stat'])
def get_stat(message):
    bot.send_message(message.chat.id, vovaSer.get_stat_punish())


@bot.message_handler(commands=['jelch'])
def make_jelch(message):
    bot.send_message(message.chat.id, vovaSer.make_punish())


@bot.message_handler(content_types=['text'])
def make_punish(message):
    if message.from_user.id == 325667968:
        aaa = random.randint(0, 7)
        date1 = message.date
        date1 = dt.fromtimestamp(date1)
        today = dt.now()
        ddd = today - date1
        if aaa == 0 and abs(ddd.total_seconds()) < 10:
            bot.send_message(message.chat.id, vovaSer.make_punish())


bot.polling()
