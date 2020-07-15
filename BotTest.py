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
vovapidr = ['Вова пидр', 'Вова гомогей', 'Вова ебоклак', 'Вова хуй', 'Вова пизда', 'Вова говной ваняет', 'Вова мразь', 'Вова хуева',
            'Вова чмо', 'Вова мудак', 'Вова такой хуевый, что дядя даже не стал его ебать', 'Вова петух', 'Вова иди нахуй']
chet = {}



# @bot.message_handler(commands=['stat'])
# def all_111(message):
#     stata = str(chet).replace("'", '').replace(':', ' -').replace(', ', '\n').replace('{', '').replace('}', '')
#     bot.send_message(message.chat.id, str(stata))


@bot.message_handler(commands=['jelch'])
def all_111(message):
    bot.send_message(message.chat.id, vovaSer.makePunish())


@bot.message_handler(content_types=['text'])
def all_text(message):
    if message.from_user.id == 325667968:
        aaa = random.randint(0, 7)
        date1 = message.date
        date1 = dt.fromtimestamp(date1)
        today = dt.now()
        ddd = today - date1
        if aaa == 0 and abs(ddd.total_seconds()) < 10:
            bot.send_message(message.chat.id, vovaSer.makePunish())
            # chet[vovapidr[ran]] = chet.get(vovapidr[ran], 0) + 1


bot.polling()
