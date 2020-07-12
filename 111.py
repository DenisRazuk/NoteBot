import telebot
import os
import random
from datetime import datetime as dt


TOKEN = '902148830:AAGUIUgNQPfJzul8WnC6INB82KtbIKQlgqE'
# JOBLIST = os.environ.get('JOBLIST')
# USERS = os.environ.get('USERS')
bot = telebot.TeleBot(TOKEN)
vovapidr = ['Вова пидр', 'Вова гомогей', 'Вова ебоклак', 'Вова хуй', 'Вова пизда', 'Вова говной ваняет', 'Вова мразь', 'Вова хуева',
            'Вова чмо', 'Вова мудак', 'Вова такой хуевый, что дядя даже не стал его ебать', 'Вова петух', 'Вова иди нахуй']
chet = {}


# @bot.message_handler(commands=['stat'])
# def all_111(message):
#     stroka = str(chet)
#     stroka = stroka.replace("'", '')
#     stroka = stroka.replace(',', '\n')
#     bot.send_message(message.chat.id, stroka)


@bot.message_handler(commands=['jelch'])
def all_111(message):
    ran1 = random.randint(0, len(vovapidr) - 1)
    bot.send_message(message.chat.id, vovapidr[ran1])
    chet[vovapidr[ran1]] = chet.get(vovapidr[ran1], 0) + 1


@bot.message_handler(content_types=['text'])
def all_text(message):
    if message.from_user.id == 325667968:
        aaa = random.randint(0, 2)
        date1 = message.date
        date1 = dt.fromtimestamp(date1)
        today = dt.now()
        ddd = today - date1
        if aaa == 0 and abs(ddd.total_seconds()) < 10:
            ran = random.randint(0, len(vovapidr) - 1)
            bot.send_message(message.chat.id, vovapidr[ran])
            chet[vovapidr[ran]] = chet.get(vovapidr[ran], 0) + 1


bot.polling()



