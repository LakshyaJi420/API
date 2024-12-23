import telebot

# Your bot's API token
API_KEY = '8062596944:AAGpjN7EVhbCgkLiLnWs6V-QlaMSLrD1TMQ'
bot = telebot.TeleBot(API_KEY)

# Your web app URL
web_app_url = 'https://username.github.io/repository'  # Replace this with your actual URL

# Command to display the main menu with a button to open the web app
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    web_button = telebot.types.KeyboardButton(
        text="Open Kar's Game",
        web_app=telebot.types.WebAppInfo(web_app_url)  # Linking the web app here
    )
    markup.add(web_button)
    bot.send_message(message.chat.id, "Welcome to Kar's Game! Click below to open the game.", reply_markup=markup)

# Run the bot
bot.polling()
