#token = 8062596944:AAGpjN7EVhbCgkLiLnWs6V-QlaMSLrD1TMQ
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace with your actual Telegram Bot API key (obtain from @BotFather)
API_KEY = "8062596944:AAGpjN7EVhbCgkLiLnWs6V-QlaMSLrD1TMQ"

# Create a TeleBot instance
bot = telebot.TeleBot(API_KEY)

# Command handler for '/start'
@bot.message_handler(commands=['start'])
def start(message):
    """
    Sends a welcome message with a button to launch the app.

    Args:
        message: The Telegram message object.
    """

    # Create an inline keyboard with a launch button
    markup = InlineKeyboardMarkup(row_width=1)  # Adjust row_width if needed
    launch_button = InlineKeyboardButton(text="Launch App", url="https://LakshyaJi420.github.io/API/")
    markup.add(launch_button)

    # Send the welcome message with the inline keyboard
    bot.send_message(
        message.chat.id,
        "Welcome! Click the button below to launch the Respiratory App:",
        reply_markup=markup
    )

# Start polling for Telegram updates
bot.polling()

