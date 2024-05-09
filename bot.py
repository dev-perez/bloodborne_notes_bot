import os
import telebot
import csv
from dotenv import load_dotenv

load_dotenv()

FILE_PATH = "./bloodborne_notes.csv"

if not os.path.exists(FILE_PATH):
    raise FileNotFoundError(
        f"The CSV file was not found at the specified path: {FILE_PATH}"
    )

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("Bot token is not defined or empty.")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome_message(message):
    """
    Sends a welcome message to the user when they start interacting with the bot.

    Parameters:
    message (telebot.types.Message): The message object.
    """
    bot.send_message(
        message.chat.id, "Welcome home, good Hunter. What is it you desire?"
    )


@bot.message_handler(commands=["notes"])
def send_note_message(message):
    """
    Sends a message asking the user to choose the number of a note.

    Parameters:
    message (telebot.types.Message): The message object.

    """
    bot.send_message(message.chat.id, "Choose a note [1 to 20]:")


def get_note_by_number(number_note):
    """
    Retrieves a note from the CSV file based on the given number.

    Parameters:
    number_note (int): The number of the note to retrieve.

    Returns:
    str: The content of the requested note, or None if not found.
    """
    with open(FILE_PATH, "r") as file:
        csv_notes = csv.reader(file, delimiter=",")
        for line in csv_notes:
            if line and line[0].isdigit():
                order_note = int(line[0])
                if order_note == number_note:
                    return line[1]
    return None


@bot.message_handler(func=lambda message: True)
def send_note(message):
    """
    Sends the requested note to the user.

    Parameters:
    message (telebot.types.Message): The message object.

    """
    if message.text.isdigit() and 1 <= int(message.text) <= 20:
        number_note = int(message.text)
        note = get_note_by_number(number_note)
        if note:
            bot.send_message(message.chat.id, f"{note}")
        else:
            bot.send_message(message.chat.id, "Note not found.")
    else:
        bot.send_message(message.chat.id, "Please choose a valid number [1 to 20].")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """
    Echoes back any message that doesn't match the predefined commands.

    Parameters:
    message (telebot.types.Message): The message object.

    """
    bot.reply_to(message, message.text)


bot.infinity_polling()
