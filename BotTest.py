import telebot
import os
import random
from datetime import datetime as dt


TOKEN = os.environ.get('TOKEN')
# JOBLIST = os.environ.get('JOBLIST')
# USERS = os.environ.get('USERS')
bot = telebot.TeleBot(TOKEN)
vovapidr = ['Вова пидр', 'Вова гомогей', 'Вова ебоклак', 'Вова хуй', 'Вова пизда', 'Вова говной ваняет', 'Вова мразь', 'Вова хуева',
            'Вова чмо', 'Вова мудак', 'Вова такой хуевый, что дядя даже не стал его ебать', 'Вова петух', 'Вова иди нахуй']
chet = {}


@bot.message_handler(commands=['stat'])
def all_111(message):
    print(chet)
    bot.send_message(message.chat.id, str(chet))


@bot.message_handler(content_types=['text'])
def all_text(message):
    if message.from_user.id == 325667968:
        aaa = random.randint(0, 2)
        print(aaa)
        date1 = message.date
        date1 = dt.fromtimestamp(date1)
        today = dt.now()
        ddd = today - date1
        if aaa == 0 and abs(ddd.total_seconds()) < 10:
            ran = random.randint(0, len(vovapidr) - 1)
            print(ran)
            bot.send_message(message.chat.id, vovapidr[ran])
            chet[vovapidr[ran]] = chet.get(vovapidr[ran], 0) + 1


bot.polling()



