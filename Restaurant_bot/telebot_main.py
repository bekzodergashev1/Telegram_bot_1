import telebot
from telebot import types

API_TOKEN = '1969507748:AAHMA0wub-Kch_NER4yroc9_fHAAyh9Y0tk'

bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add('1', '2') #Имена кнопок
    markup.add('3', '4') #Имена кнопок
    msg = bot.reply_to(message, 'Assalomu alaykum!', reply_markup=markup)
    bot.register_next_step_handler(msg, process_step)

def process_step(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add('🛍Buyurtma qilish') #Имена кнопок
    markup.add('🛒Savat', '⚙Sozlamalar') #Имена кнопок

    if message.text=='1':
        msg = bot.reply_to(message, 'Test text 1', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)

    elif message.text == '2':
        msg = bot.reply_to(message, 'Test text 2', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    elif message.text == '3':
        msg = bot.reply_to(message, 'Test text 3', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)

    elif message.text == '4':
        msg = bot.reply_to(message, 'Test text 4', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)


bot.polling()