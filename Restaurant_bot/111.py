if query.data == 'stollar':
    keyboard = [
        [
            InlineKeyboardButton('Lux1', callback_data='lux1'),
            InlineKeyboardButton('lux2', callback_data='lux2'),
        ],
        [
            InlineKeyboardButton('Family1', callback_data='family1'),
            InlineKeyboardButton('Family2', callback_data='family2'),
        ],
    ]

elif query.data == 'lux1':
    keyboard = [
        [
            InlineKeyboardButton('Orqaga', callback_data='stollar')
        ]
    ]
    query.message.reply_text(text='<b>4 kishilik joy</b> 👇')
elif query.data == 'lux2':
    keyboard = [
        [
            InlineKeyboardButton('Orqaga', callback_data='stollar')
        ]
    ]
    query.message.reply_text(text='<b>6 kishilik joy</b> 👇')
elif query.data == 'family1':
    keyboard = [
        [
            InlineKeyboardButton('Orqaga', callback_data='stollar')
        ]
    ]
    query.message.reply_text(text='<b>4 kishilik joy</b> 👇')
elif query.data == 'family2':
    keyboard = [
        [
            InlineKeyboardButton('Orqaga', callback_data='stollar')
        ]
    ]
    query.message.reply_text(text='<b>6 kishilik joy</b> 👇')

if query.data == 'taomlar':
    keyboard = [
        [
            InlineKeyboardButton('Shashlik', callback_data='shashlik'),
            InlineKeyboardButton('Osh', callback_data='osh'),
        ],
        [
            InlineKeyboardButton('Sho\'rva', callback_data='shurva'),
            InlineKeyboardButton('Non', callback_data='non'),
        ],
    ]

elif query.data == 'shashlik':
    keyboard = [
        [
            InlineKeyboardButton('Orqaga', callback_data='taomlar')
        ]
    ]
    query.message.reply_text(text='<b>Shashlik</b> 👇')
elif query.data == 'osh':
    keyboard = [
        [
            InlineKeyboardButton('Orqaga', callback_data='taomlar')
        ]
    ]
    query.message.reply_text(text='<b>Osh</b> 👇')
elif query.data == 'shurva':
    keyboard = [
        [
            InlineKeyboardButton('Orqaga', callback_data='taomlar')
        ]
    ]
    query.message.reply_text(text='<b>Sho\'rva</b> 👇')
elif query.data == 'non':
    keyboard = [
        [
            InlineKeyboardButton('Orqaga', callback_data='taomlar')
        ]
    ]
    query.message.reply_text(text='<b>Non</b> 👇')