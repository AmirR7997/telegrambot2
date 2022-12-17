import telebot
import sqlite3

TOKEN = "5958081967:AAFSDhG4CshOZqHKCIq9VFzQ-fJnHNuBjqg"

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def greetings(message):
    reply = "Hello i am a simple data collection bot"
    bot.reply_to(message, reply)


    if message.text == '/show data':
        data = read_data_from_db()
        for datum in data:
            bot.reply_to(message, str(datum))


is_taking_address = False
is_taking_phone = False
is_taking_surname = False
is_taking_name = False
name = None
surname = None
phone = None
address = None
@bot.message_handler(content_types=['text'])
def message_handler(message):
    chat_id = message.chat.id
    global is_taking_name
    global is_taking_surname
    global is_taking_phone
    global is_taking_address
    global name
    global surname
    global phone
    global address



    if is_taking_name:

        name = message.text
        print(name)
        is_taking_name = False

    if is_taking_surname:
        surname = message.text
        print(surname)
        is_taking_surname = False

    if is_taking_phone:
        phone = message.text
        print(phone)
        is_taking_phone = False

    if is_taking_address:
        address = message.text
        print(address)
        is_taking_address = False
        save_data_to_db(name, surname, phone, address)

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

def save_data_to_db(name, surname, phone, address):

    connection = None

    try:
        connection = sqlite3.connect("db_telegrambot2")
        cursor = connection.cursor()

        insert_sql = f"""INSERT INTO 
                    telegrambot2 (name, surname, phone, address)
                    VALUES ('{name}', '{surname}', '{phone}', '{address}')"""
        cursor.execute(insert_sql)
        connection.commit()
        connection.close()
    except Exception as e:
        print("There was an error in the database! ")
        print(e)

def read_data_from_db():
    try:
        connection = sqlite3.connect("db_telegrambot2")
        cursor = connection.cursor()

        select_sql = """
        SELECT * FROM telegrambot2
        """
        cursor.execute(select_sql)
        connection.commit()

        data = cursor.fetchall()

        connection.close()
        return data
    except Exception as e:
        print("There was an error in the database! ")
        print(e)



bot.infinity_polling()
