import telebot
mas = []
num = []


bot = telebot.TeleBot("1493631859:AAFHRluKTcxqFKfyrK4GrJOtalCRqPKGWXQ")

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('/начало', '/помощь', '/заказ')
keyboard1.row('/меню', '/мой_заказ', '/оформить')


keyboardpro = telebot.types.ReplyKeyboardMarkup()
keyboardpro.row('/пепперони', '/ветчина_и_грибы', '/сырная')
keyboardpro.row('/гавайская', '/пицца_с_морепродуктами')
keyboardpro.row('/coca_cola', '/sprite', '/fanta', '/клюквенный_морс')
keyboardpro.row('/вода_с_газом', '/вода_без_газа')
keyboardpro.row('/основная_клавиатура')


keyboardphone = telebot.types.ReplyKeyboardMarkup(True)
keyboardphone.row('/1', '/2', '/3')
keyboardphone.row('/4', '/5', '/6')
keyboardphone.row('/7', '/8', '/9')
keyboardphone.row('/0','/Удалить_цифру', '/Я_ввел(а)_свой_номер')


keyboardlast1 = telebot.types.ReplyKeyboardMarkup(True)
keyboardlast1.row('/Я_все_отправил(а)!!', '/в_начало',"/отправить_мой_заказ_менеждеру",'/отправить_номер_телефона_менеджеру')


@bot.message_handler(commands=['start', 'начало','в_начало'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я телеграмм бот по заказу пиццы. \n' +
                 'Давай познакомимся с командами которые ты можешь прописывать :\n' +
                 '1) /в_начало - эта команда будет запускать меня снова и снова \n' +
                 '2) /помощь - если у тебя что-то не получается то позови меня и я тебе помогу \n ' +
                 '3) /меню - эта команда открывает меню:\n' +
                 '4) /заказ - данная команда высветит тебе сразу все позиции чтобы ты смог сделать свой заказ\n' +
                 '5) /мой_заказ - данная команда покажет тебе то что ты уже заказал.\n'+
                 '6) /оформить - тут ты сможешь оформить свой заказ',
                     reply_markup=keyboard1)

@bot.message_handler(commands=['основная_клавиатура'])
def star(message):
    bot.send_message(message.chat.id, 'Возвращаю основную клавиатуру',reply_markup=keyboard1)

@bot.message_handler(commands=['меню'])
def menu(message):
    bot.send_message(message.chat.id,
                     'Это наше меню для пицц! Скажи когда будешь готов сделать заказ!\n' +
                     '1) Пепперони.\n' +
                     '2) Ветчина и грибы.\n' +
                     '3) Сырная.\n' +
                     '4) Гавайская.\n' +
                     '5) Пицца с морепродуктами.\n' +
                     '6) Coca Cola.\n' +
                     '7) Sprite.\n' +
                     '8) Fanta.\n' +
                     '9) Клюквенный морс.\n' +
                     '10) Вода с газом.\n' +
                     '11) Вода без газа.',
                        reply_markup=keyboardpro)

@bot.message_handler(commands=['пепперони'])
def start_message(message):
    bot.send_photo(message.chat.id, 'https://yadi.sk/i/S10KsyMMGmwD7g')

@bot.message_handler(commands=['ветчина_и_грибы'])
def start_message(message):
    bot.send_photo(message.chat.id, 'https://yadi.sk/i/qtn6nqMXY8Ns-A')

@bot.message_handler(commands=['сырная'])
def start_message(message):
    bot.send_photo(message.chat.id, 'https://yadi.sk/i/zIhz49Pd83gq8w')

@bot.message_handler(commands=['гавайская'])
def start_message(message):
    bot.send_photo(message.chat.id, 'https://yadi.sk/i/3KhGN6hGOzfvBA')

@bot.message_handler(commands=['пицца_с_морепродуктами'])
def start_message(message):
    bot.send_photo(message.chat.id, 'https://yadi.sk/i/vcSnRw5JXsfU_w')

@bot.message_handler(commands=['coca_cola'])
def start_message(message):
    bot.send_photo(message.chat.id, 'https://yadi.sk/i/CgqIQ_onowqMbg')

@bot.message_handler(commands=['sprite'])
def start_message(message):
    bot.send_photo(message.chat.id, 'https://yadi.sk/i/OGKKQH0SbSUfuA')

@bot.message_handler(commands=['fanta'])
def start_message(message):
    bot.send_photo(message.chat.id, 'https://yadi.sk/i/RMqnR4SsZqJQrQ')

@bot.message_handler(commands=['клюквенный_морс'])
def start_message(message):
    bot.send_photo(message.chat.id, 'https://yadi.sk/i/wZoGvIec1tXzBg')

@bot.message_handler(commands=['вода_с_газом'])
def start_message(message):
    bot.send_photo(message.chat.id, 'https://yadi.sk/i/g1lwY7YU95xIUw')

@bot.message_handler(commands=['вода_без_газа'])
def start_message(message):
    bot.send_photo(message.chat.id, 'https://yadi.sk/i/WodzphpsIMBLaQ')

@bot.message_handler(commands=['заказ'])
def buttons(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Пепперони', callback_data='Пепперони'),
        telebot.types.InlineKeyboardButton('Ветчина и грибы', callback_data='Ветчина и грибы'),
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Сырная', callback_data='Сырная'),
        telebot.types.InlineKeyboardButton('Гавайская', callback_data='Гавайская'),
        telebot.types.InlineKeyboardButton('Пицца с морепродуктами', callback_data='Пицца с морепродуктами'),
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Coca Cola', callback_data='Coca Cola'),
        telebot.types.InlineKeyboardButton('Sprite', callback_data='Sprite'),
        telebot.types.InlineKeyboardButton('Fanta', callback_data='Fanta'),
    )
    keyboard.row(
    telebot.types.InlineKeyboardButton('Клюквенный морс', callback_data='Клюквенный морс'),
    telebot.types.InlineKeyboardButton('Вода с газом', callback_data='Вода с газом'),
    telebot.types.InlineKeyboardButton('Вода без газа', callback_data='Вода без газа'),
    )
    bot.send_message(
        message.chat.id,
        'Сделайте пожалуйста свой заказ:',
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    if c.data == 'Пепперони':
        mas.append(c.data)
        bot.send_message(c.message.chat.id, 'Добавлено к заказу')
    if c.data == 'Ветчина и грибы':
        mas.append(c.data)
        bot.send_message(c.message.chat.id, 'Добавлено к заказу')
    if c.data == 'Сырная':
        mas.append(c.data)
        bot.send_message(c.message.chat.id, 'Добавлено к заказу')
    if c.data == 'Гавайская':
        mas.append(c.data)
        bot.send_message(c.message.chat.id, 'Добавлено к заказу')
    if c.data == 'Пицца с морепродуктами':
        mas.append(c.data)
        bot.send_message(c.message.chat.id, 'Добавлено к заказу')
    if c.data == 'Coca Cola':
        mas.append(c.data)
        bot.send_message(c.message.chat.id, 'Добавлено к заказу')
    if c.data == 'Sprite':
        mas.append(c.data)
        bot.send_message(c.message.chat.id, 'Добавлено к заказу')
    if c.data == 'Fanta':
        mas.append(c.data)
        bot.send_message(c.message.chat.id, 'Добавлено к заказу')
    if c.data == 'Клюквенный морс':
        mas.append(c.data)
        bot.send_message(c.message.chat.id, 'Добавлено к заказу')
    if c.data == 'Вода с газом':
        mas.append(c.data)
        bot.send_message(c.message.chat.id, 'Добавлено к заказу')
    if c.data == 'Вода без газа':
        mas.append(c.data)
        bot.send_message(c.message.chat.id, 'Добавлено к заказу')

@bot.message_handler(commands=['мой_заказ'])
def help_command(message):
    try:
        s=''
        for i in mas:
            s+= i + '\n'
        bot.send_message(message.chat.id,s)
    except:
        bot.send_message(message.chat.id,"Ваша корзина пока пуста. Вы можете зайти в меню и посмотреть картинки пицц после чего заказать всё, что вы хотите")

@bot.message_handler(commands=['оформить'])
def ordering(message):
    bot.send_message(message.chat.id,'Начнем оформление заказа!! На этой стадии вы должны отправить свой заказ, а так же ввести и отправить номер телефона для связи. Введите пожалуйста свой номер телефона:',reply_markup=keyboardphone)

@bot.message_handler(commands=['1'])
def ordering(message):
    a='1'
    num.append(a)
    bot.send_message(message.chat.id,'Я запомнил цифру.Продолжайте вводить свой номер')

@bot.message_handler(commands=['2'])
def ordering(message):
    b='2'
    num.append(b)
    bot.send_message(message.chat.id,'Я запомнил цифру.Продолжайте вводить свой номер')

@bot.message_handler(commands=['3'])
def ordering(message):
    c='3'
    num.append(c)
    bot.send_message(message.chat.id,'Я запомнил цифру.Продолжайте вводить свой номер')

@bot.message_handler(commands=['4'])
def ordering(message):
    d = '4'
    num.append(d)
    bot.send_message(message.chat.id, 'Я запомнил цифру.Продолжайте вводить свой номер')

@bot.message_handler(commands=['5'])
def ordering(message):
    e = '5'
    num.append(e)
    bot.send_message(message.chat.id, 'Я запомнил цифру.Продолжайте вводить свой номер')

@bot.message_handler(commands=['6'])
def ordering(message):
    f = '6'
    num.append(f)
    bot.send_message(message.chat.id, 'Я запомнил цифру.Продолжайте вводить свой номер')

@bot.message_handler(commands=['7'])
def ordering(message):
    g = '7'
    num.append(g)
    bot.send_message(message.chat.id, 'Я запомнил цифру.Продолжайте вводить свой номер')

@bot.message_handler(commands=['8'])
def ordering(message):
    h = '8'
    num.append(h)
    bot.send_message(message.chat.id, 'Я запомнил цифру.Продолжайте вводить свой номер')

@bot.message_handler(commands=['9'])
def ordering(message):
    j = '9'
    num.append(j)
    bot.send_message(message.chat.id, 'Я запомнил цифру.Продолжайте вводить свой номер')

@bot.message_handler(commands=['0'])
def ordering(message):
    k = '0'
    num.append(k)
    bot.send_message(message.chat.id, 'Я запомнил цифру.Продолжайте вводить свой номер')

@bot.message_handler(commands=['Удалить_цифру'])
def deliter(message):
    del num[-1]
    d = ''
    for i in num:
        d += i
    bot.send_message(message.chat.id, d,)

@bot.message_handler(commands=['Я_ввел(а)_свой_номер'])
def ordering(message):
    d = ''
    for i in num:
        d += i
    bot.send_message(message.chat.id,d,reply_markup=keyboardlast1)



@bot.message_handler(commands=['отправить_номер_телефона_менеджеру'])
def ordering(message):
    try:
        d = ''
        for i in num:
            d += i
        bot.send_message(1206703222, d,)
    except:
        bot.send_message(message.chat.id,"Вы не ввели свой номер. Попробуйте ещё раз!")

@bot.message_handler(commands=['отправить_мой_заказ_менеждеру'])
def ordering(message):
    try:
        s = ''
        for i in mas:
            s += i + '\n'
        bot.send_message(1206703222,s, reply_markup=keyboardlast1)
    except:
        bot.send_message(message.chat.id,"Ваша корзина пока пуста. Вы можете зайти в меню и посмотреть картинки пицц после чего заказать всё, что вы хотите",reply_markup=keyboard1)

@bot.message_handler(commands=['Я_все_отправил(а)!!'])
def ordering(message):
    keyboardlast1 = telebot.types.InlineKeyboardMarkup()
    keyboardlast1.add(
        telebot.types.InlineKeyboardButton(
            'Ссылка для связи с разработчиком', url='https://t.me/user_abraham'
        )
    )
    bot.send_message(
        message.chat.id,
        "Круто!! Теперь остается только ждать пока с вами свяжется менеджер и обговорит все детали заказа! Обычно это происходит в течение 5 минут так что не уберайте телефон далеко)) Если у вас есть какие-либо вопросы то выможете задать их тут) \n ",
        reply_markup=keyboardlast1
    )


@bot.message_handler(commands=['помощь'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Ссылка для связи с разработчиком', url='https://t.me/user_abraham'
        )
    )
    bot.send_message(
        message.chat.id,
        "Проверьте правильность введенной команды. Все команды должны писаться через знак '/' !! \n " +
        "Если это не помогло то вызовите команду /начало . Эта команда покажет вам полный перечень всевозможных команд \n" +
        "Так же ты можешь написать разработчику кликнув по кнопке, которая расположена ниже",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Возможно ты что-то написал не так 🤔. Учти что все команды вводятся через символ '/' !!\n"+
        " Если что, ты можешь вызвать функцию /помощь , где тебе все объяснят")

bot.polling()