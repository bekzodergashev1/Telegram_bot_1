from telegram import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, message
from telegram.ext import (Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters)

BTN_BUYURTMA, BTN_SAVAT, BTN_SOZLAMA = ('🛍Buyurtma qilish', '🛒Savat', '⚙Sozlamalar')
main_buttons = ReplyKeyboardMarkup([
    [BTN_BUYURTMA], [BTN_SAVAT, BTN_SOZLAMA]
], resize_keyboard=True)
BTN_1, BTN_2, BTN_3, BTN_4, BTN_5, BTN_6, BTN_7, BTN_8, BTN_9, BTN_10, BTN_11, BTN_12 = (
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')

# table_buttons = ReplyKeyboardMarkup([
#     [BTN_1, BTN_2, BTN_3, BTN_4, BTN_5, BTN_6], [BTN_7, BTN_8, BTN_9, BTN_10, BTN_11, BTN_12]
# ], resize_keyboard=True)

menu_buttons = ReplyKeyboardMarkup([
    [BTN_1, BTN_2, BTN_3, BTN_4, BTN_5, BTN_6], [BTN_7, BTN_8, BTN_9, BTN_10, BTN_11, BTN_12]
], resize_keyboard=True)

STATE_MAIN = 1
STATE_BUYURTMA = 2

buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton('Menu', callback_data='menu'),
            # InlineKeyboardButton('Stollar', callback_data='stollar'),
        ]
    ])

def start(update, context):
    user = update.message.from_user


    update.message.reply_html(
        'Assalomu alaykum <b>{}!</b>\n \nRestaurant botiga hush kelibsiz😊\n \n<b>Quyidagilardan birini tanlang</b> 👇'.
        format(user.first_name), reply_markup=main_buttons)
    return STATE_BUYURTMA


def inline_callback(update, context):
    query = update.callback_query
    query.message.delete()
    if query.data == "menu":
                    # Text yoziladi menu uchun
        query.message.reply_html(text='<b>Menu royhati!</b>', reply_markup=menu_buttons)
        photo_path = 'images/{}.jpg'
        update.message.reply_photo(photo=open(photo_path, 'rb'), caption=message, reply_markup=menu_buttons)
    # elif query.data == "stollar":
    #                 # Text yoziladi stollar uchun
    #     query.message.reply_html(text='<b> 🔻    Stollar royhat!  🔻\n'
    #                                   '1️⃣ Oddiy_2   2️⃣ Oddiy_4   3️⃣ Oddiy_6\n'
    #                                   '4️⃣ Kobinka_2  5️⃣ Kobinka_4  6️⃣ Kobinka_6\n'
    #                                   '7️⃣ Family_4  8️⃣ Family_6  9️⃣ Family_8\n'
    #                                   '1️⃣0️⃣ Lux_4  1️⃣1️⃣ Lux_6  1️⃣2️⃣ Lux_8\n</b>', reply_markup=table_buttons)

    return STATE_MAIN


def buyurtmalar(update, context):
    update.message.reply_text('Menyular ro\'yhati 🥗\n ', reply_markup=buttons)


def savat(update, context):
    update.message.reply_text('Savat belgilandi')


def sozlama(update, context):
    update.message.reply_text('Sozlama belgilandi')


def main():
    # updater ornatib olamiz
    updater = Updater('1969507748:AAHMA0wub-Kch_NER4yroc9_fHAAyh9Y0tk', use_context=True)

    # Dispatcher eventlarni aniqlash uchun
    dispatcher = updater.dispatcher

    # start komandasini ushlab qolish
    # dispatcher.add_handler(CommandHandler('start', start))

    # inline button query
    dispatcher.add_handler(CallbackQueryHandler(inline_callback))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            STATE_MAIN: [CallbackQueryHandler(inline_callback)],
            STATE_BUYURTMA: [
                MessageHandler(Filters.regex('^('+BTN_BUYURTMA+')$'), buyurtmalar),
                MessageHandler(Filters.regex('^('+BTN_SOZLAMA+')$'), sozlama),
                MessageHandler(Filters.regex('^('+BTN_SAVAT+')$'), savat),
            ],
        },
        fallbacks=[CommandHandler('start', start)]
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


main()
