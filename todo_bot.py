from random import choice

import telebot

token = "2034828026:AAEq_llWITaM5_ue6DT8dwNpry6FXBxYLDI"
bot = telebot.TeleBot(token)

Random_tasks = ["Прочитать 20 страниц", "Посмотреть обучающий видеокурс", "Выполнить практику по изученному материалу"]

todos = dict()

HELP = '''
Список доступных команд:
/ print  - напечать все добавленные задачи
/ todo - добавить задачу
/ random - добавить на сегодня случайную задачу
/ help - Напечатать список доступных команд
'''

def add_todo(date, task):
    date = date.lower()
    if todos.get(date) is not None:
        todos[date].append(task)
    else:
        todos[date] = [task]


@bot.message.handler(commands=['help'])
def help(message):
    bot.send.message(message.chat.id, HELP)


@bot.message.handler(commands=['random'])
def random(message):
    task = choice(Random_tasks)
    add_todo('сегодня', task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на сегодня!')


@bot.message.handler(commands=['todo'])
def todo(message):
    _, date, tail = message.text.split(maxsplit=2)
    task = ' '.join([tail])
    add_todo(date, task)
    bot.send_message(message.chat.id, f'{date} - {task} задача добавлена!')


@bot.message.handler(commands=['print'])
def printf(message):
    date = message.text.split()[1].lower()
    if date in todos:
        tasks = ""
        for task in todos[date]:
            tasks += f'{task}\n'
    else:
        tasks = "Такой даты нет"
        bot.send_message(message.chat.id, tasks)


bot.polling(none_stop=True)