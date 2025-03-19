import telebot
from telebot import types

bot = telebot.TeleBot('7743190373:AAHyNDAgLPaN2TLUIIEG2SQdjBLX5dYsEEg')

# @bot.message_handler(content_types=['text'])
# def get_text_message(message):
#     if message.text == 'Привет':
#         bot.send_message(message.from_user.id, 'Привет, чем могу помочь?')
#     elif message.text == '/help':
#         bot.send_message(message.from_user.id, 'Напиши привет')
#     elif message.text == '52':
#         bot.send_message(message.from_user.id, 'АООВОАОЫОАЫ 52 52')
#     else:
#         bot.send_message(message.from_user.id, 'Я тебя не понимаю')
        
# bot.polling(none_stop = True, interval = 0)

name = ''
surname = ''
age = 0
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, 'Как тебя зовут?')
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')
        
def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)
    
def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько лет тебе?')
    bot.register_next_step_handler(message, get_age)
    
def get_age(message):
    global age
    try:
        age = int(message.text)
        bot.send_message(message.from_user.id, 'Тебе' + ' '+ str(age) + ' ' + 'лет, тебя зовут' + ' ' + name + ' ' + surname + '?')
    except ValueError:
        bot.send_message(message.from_user.id, 'Цифрами пиши, сколько лет то?')
        bot.register_next_step_handler(message, get_age)
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Тебе' + ' '+ str(age) + ' ' + 'лет, тебя зовут' + ' ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, 'Запомню ;))')
    if call.data == 'no':
        bot.send_message(call.message.chat.id, 'Я тебя убью ща xddd')
        
bot.polling(none_stop = True, interval= 0)