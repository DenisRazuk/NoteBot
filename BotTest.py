import telebot
from telebot import types
import json
import urllib.request
import requests
import logging
from flask import Flask, request
import os

bot = telebot.TeleBot('902148830:AAF5Qg73b5P1rSM3kCPzolyvAX_XsS_dYaI')

num_chat = {}
task_desc = {}

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Да', 'Нет')


def check_user(message):
    if message.chat.id not in num_chat:
        bot.send_message(message.chat.id, 'Введи /start для регистрации')
        res = False
    else:
        res = True
    return res


@bot.message_handler(commands=['start'])
def phone(message):
    if message.chat.id not in num_chat:
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
        keyboard.add(button_phone)
        bot.send_message(message.chat.id, 'Для регистрации необходим номер телефона', reply_markup=keyboard)


@bot.message_handler(content_types=['contact'])
def read_phone(message):
    if num_chat.get(message.contact.phone_number) is None:
        num_chat[int(message.chat.id)] = int(message.contact.phone_number.replace('+', ''))
        new_phone = int(message.contact.phone_number.replace('+', ''))
        pyt_q = {"id": new_phone, "telegramId": int(message.chat.id)}
        json_q = json.dumps(pyt_q)
        r = requests.post('https://aoverinapp.herokuapp.com/users', json=json_q)
        q = requests.get('https://aoverinapp.herokuapp.com/users', data=["id"])
        print(q.text)

        # url = 'https://aoverinapp.herokuapp.com/users'
        # data = {message.contact.phone_number, message.chat.id}
        # data_json = json.dumps(data)
        # payload = {'json_payload': data_json}
        # req = requests.get(url, data = payload)


# @bot.message_handler(content_types=['text'])
# def num_phone(message):
#     if message.text
#     bot.send_message(message.chat.id, 'Добавить задачу с названием ' + message.text)

@bot.message_handler(content_types=['text'])
def all_text(message):
    if check_user(message):
        if message.text not in ('Да', 'Нет'):
            task_desc[message.chat.id] = message.text
        if message.text not in ('Да', 'Нет'):
            bot.send_message(message.chat.id, 'Добавить задачу?', reply_markup=keyboard1)
        elif message.text == 'Да':
            pyt_q = {"id": num_chat[message.chat.id], "title": "Telegram", "description": task_desc[message.chat.id]}
            json_q = json.dumps(pyt_q)
            r = requests.post('https://aoverinapp.herokuapp.com/joblists', json=json_q)
            bot.send_message(message.chat.id, 'Задача добавлена')
            print(json_q)
            task_desc[message.chat.id] = ''
            print(task_desc)
        elif message.text == 'Нет':
            bot.send_message(message.chat.id, 'Окей(')
            task_desc[message.chat.id] = ''
            print(task_desc)




# Запрос на отпрвку в апишку
# title_text = message.text
# bot.send_message(message.chat.id, 'Введите описание задачи')
# response = urllib.request.urlopen('https://aoverinapp.herokuapp.com/users')
#             # print(response.read())
#             # response.close()


# if "HEROKU" in list(os.environ.keys()):
    # #     logger = telebot.logger
    # #     telebot.logger.setLevel(logging.INFO)
    # #
    # #     server = Flask(__name__)
    # #     @server.route("/bot", methods=['POST'])
    # #     def getMessage():
    # #         bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    # #         return "!", 200
    # #     @server.route("/")
    # #     def webhook():
    # #         bot.remove_webhook()
    # #         bot.set_webhook(url="https://aoverinapp.herokuapp.com/")
    # #         return "?", 200
    # #     server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
    # # else:
    # #     # если переменной окружения HEROKU нету, значит это запуск с машины разработчика.
    # #     # Удаляем вебхук на всякий случай, и запускаем с обычным поллингом.
    # #     bot.remove_webhook()
bot.polling()
