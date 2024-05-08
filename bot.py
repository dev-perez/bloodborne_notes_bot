import os
import telebot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
if BOT_TOKEN is None:
    raise Exception("Bot token is not defined")


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, "Welcome home, good Hunter. What is it you desire?")



@bot.message_handler(commands=["notes"])
def send_notes(message):
    try:
        bot.send_message(message.chat.id, "Choose a note [1 to 20]:")
        bot.register_next_step_handler(message, handle_notes)
    except:
        bot.send_message(message.chat.id, "Please choose a valid number.")


def handle_notes(message):
    try:
        number = int(message.text)
        bot.send_message(message.chat.id, f"You choose number is: {number}")
    except ValueError:
        bot.send_message(message.chat.id, "Please choose a valid number.")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
