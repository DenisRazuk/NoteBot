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
vova_id = os.environ.get('vova_id')
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
    if message.from_user.id == int(vova_id):
        if vovaSer.need_send(message.date):
            bot.send_message(message.chat.id, vovaSer.make_punish())


bot.polling()
