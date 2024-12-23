#token = 8062596944:AAGpjN7EVhbCgkLiLnWs6V-QlaMSLrD1TMQ
from telebot import TeleBot, types

# Initialize the bot
API_KEY = "8062596944:AAGpjN7EVhbCgkLiLnWs6V-QlaMSLrD1TMQ"  # Replace with your actual API key
bot = TeleBot(API_KEY)

# Command to start the bot
@bot.message_handler(commands=['start'])
def start(message):
    # Create a menu with buttons
    markup = types.InlineKeyboardMarkup()
    launch_button = types.InlineKeyboardButton(
        text="Launch App", url="https://LakshyaJi420.github.io/API/"  # Use the GitHub Pages URL
    )
    markup.add(launch_button)
    
    bot.send_message(
        message.chat.id, 
        "Welcome to Kar's Game! Click the button below to launch the app:",
        reply_markup=markup
    )

# Run the bot
bot.polling()
