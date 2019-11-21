import telebot
from telebot import types
import json
import requests
import os
from flask import Flask, request

print(os.environ.get('TOKEN'))
bot = telebot.TeleBotos.os.environ('TOKEN')
# ('902148830:AAF5Qg73b5P1rSM3kCPzolyvAX_XsS_dYaI')

server = Flask(__name__)

num_chat = {}
task_desc = {}



# r = requests.get('https://aoverinapp.herokuapp.com/users', data = {"id": "telegtamd"})
# pars = json.loads(r.text)
# print(pars)
# print(r)
# print(data)


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


@bot.message_handler(commands=['task'])
def task(message):
    if check_user(message):
        headers = {'content-type': 'application/json'}
        r = requests.get('https://aoverinapp.herokuapp.com/joblists', params={"id": num_chat.get(message.chat.id)}, headers=headers)
        pars = json.loads(r.text)
        for raspars in pars:
            bot.send_message(message.chat.id, str(raspars.get('description')))


@bot.message_handler(content_types=['contact'])
def read_phone(message):
    if num_chat.get(message.contact.phone_number) is None:
        headers = {'content-type': 'application/json'}
        num_chat[int(message.chat.id)] = int(message.contact.phone_number.replace('+', ''))
        new_phone = int(message.contact.phone_number.replace('+', ''))
        pyt_q = {"id": new_phone, "telegramId": int(message.chat.id)}
        json_q = json.dumps(pyt_q)
        r = requests.post('https://aoverinapp.herokuapp.com/users', data=json_q, headers=headers)
        # q = requests.get('https://aoverinapp.herokuapp.com/users', data=["id"])
        # print(q.text)
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
            headers = {'content-type': 'application/json'}
            pyt_q = {"id": num_chat[message.chat.id], "title": "Telegram", "description": task_desc[message.chat.id]}
            json_q = json.dumps(pyt_q)
            bot.send_message(message.chat.id, 'Одну минуточку)')
            r = requests.post('https://aoverinapp.herokuapp.com/joblists', data=json_q,  headers=headers)
            bot.send_message(message.chat.id, 'Задача добавлена')
            task_desc[message.chat.id] = None
        elif message.text == 'Нет':
            bot.send_message(message.chat.id, 'Окей(')
            task_desc[message.chat.id] = None
            print(task_desc)


# TODO Сделать тест webhook
# TODO Сделать сбор num_chat перед запуском с БД
# TODO Переделать чек на запрос в API


# Запрос на отпрвку в апишку
# title_text = message.text
# bot.send_message(message.chat.id, 'Введите описание задачи')
# response = urllib.request.urlopen('https://aoverinapp.herokuapp.com/users')
#             # print(response.read())
#             # response.close()

bot.polling()


# @server.route("/")
# def webhook():
#     bot.remove_webhook()
#     bot.set_webhook(url="https://limitless-cliffs-44855.herokuapp.com/902148830:AAF5Qg73b5P1rSM3kCPzolyvAX_XsS_dYaI")
#     return "!", 200
#
#
# server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


