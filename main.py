import telebot

TOKEN = "5958081967:AAFSDhG4CshOZqHKCIq9VFzQ-fJnHNuBjqg"

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def greetings(message):
    reply = "Hello i am a simple data collection bot"
    bot.reply_to(message, reply)



is_taking_address = False
is_taking_phone = False
is_taking_surname = False
is_taking_name = False
@bot.message_handler(content_types=['text'])
def message_handler(message):
    chat_id = message.chat.id
    global is_taking_name
    global is_taking_surname
    global is_taking_phone
    global is_taking_address

    if is_taking_name:

        user_name = message.text
        print(user_name)
        is_taking_name = False

    if is_taking_surname:
        user_surname = message.text
        print(user_surname)
        is_taking_surname = False

    if is_taking_phone:
        user_phone = message.text
        print(user_phone)
        is_taking_surname = False
    if is_taking_address:
        user_address = message.text
        print(user_address)
        is_taking_address = False

    if message.text == 'Save name':
        is_taking_name = True
        bot.send_message(chat_id, "Input your Name: ")
    if message.text == 'Save surname':
        is_taking_surname = True
        bot.send_message(chat_id, "Input your Surname: ")
    if message.text == 'Save phone':
        is_taking_phone = True
        bot.send_message(chat_id, "Input your phone number: ")
    if message.text == 'Save address':
        is_taking_address = True
        bot.send_message(chat_id, "Input your address: ")

bot.infinity_polling()
