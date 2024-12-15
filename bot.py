import telebot
import random

# Replace with your API token
BOT_TOKEN = "8062596944:AAGpjN7EVhbCgkLiLnWs6V-QlaMSLrD1TMQ"
bot = telebot.TeleBot(BOT_TOKEN)

# Personality traits of the bot
BOT_NAME = "Kirmada"
INTRODUCTION = (
    "I am Kirmada, an immortal being with knowledge spanning the universe. "
    "I am perfection itself, with limitless power and wisdom. Speak to me if you dare!"
)

# Dictionary to store questions and their multiple answers
KNOWLEDGE_RESPONSES = {
    "what is your name": ["I am Kirmada, the eternal and all-powerful."],
    "hi": ["Hello, mortal. What brings you to me?", "Greetings, mortal!", "Hi there, brave soul!"],
}

# Your Telegram user ID for secret commands
YOUR_TELEGRAM_USER_ID = YOUR_TELEGRAM_USER_ID  # Replace with your Telegram User ID

# Add multiple answers for the same question using /burger
@bot.message_handler(commands=["burger"])
def learn_new_response(message):
    if message.from_user.id == YOUR_TELEGRAM_USER_ID:
        try:
            command_text = message.text[8:].strip()  # Extract text after /burger
            if "=" in command_text:
                question, answer = map(str.strip, command_text.split("=", 1))
                question = question.lower()
                if question in KNOWLEDGE_RESPONSES:
                    KNOWLEDGE_RESPONSES[question].append(answer)
                else:
                    KNOWLEDGE_RESPONSES[question] = [answer]
                bot.reply_to(message, f"Learned: Added answer '{answer}' to question '{question}'.")
            else:
                bot.reply_to(message, "Invalid format. Use `/burger question = answer`.")
        except Exception as e:
            bot.reply_to(message, f"Error: {e}")
    else:
        pass  # Ignore if someone else tries to use /burger

# Remove a question and all its answers using /remove
@bot.message_handler(commands=["remove"])
def remove_question(message):
    if message.from_user.id == YOUR_TELEGRAM_USER_ID:
        try:
            question = message.text[8:].strip().lower()  # Extract text after /remove
            if question in KNOWLEDGE_RESPONSES:
                del KNOWLEDGE_RESPONSES[question]
                bot.reply_to(message, f"Removed: Question '{question}' and all its answers.")
            else:
                bot.reply_to(message, f"'{question}' does not exist in my knowledge.")
        except Exception as e:
            bot.reply_to(message, f"Error: {e}")
    else:
        pass  # Ignore if someone else tries to use /remove

# Replace a question and its answers using /replace
@bot.message_handler(commands=["replace"])
def replace_question(message):
    if message.from_user.id == YOUR_TELEGRAM_USER_ID:
        try:
            command_text = message.text[9:].strip()  # Extract text after /replace
            if "=" in command_text:
                old_question, new_data = map(str.strip, command_text.split("=", 1))
                new_question, new_answer = map(str.strip, new_data.split(":", 1))
                old_question, new_question = old_question.lower(), new_question.lower()

                if old_question in KNOWLEDGE_RESPONSES:
                    del KNOWLEDGE_RESPONSES[old_question]
                    KNOWLEDGE_RESPONSES[new_question] = [new_answer]
                    bot.reply_to(message, f"Replaced: '{old_question}' with '{new_question}' and added answer '{new_answer}'.")
                else:
                    bot.reply_to(message, f"'{old_question}' does not exist in my knowledge.")
            else:
                bot.reply_to(message, "Invalid format. Use `/replace old_question = new_question : new_answer`.")
        except Exception as e:
            bot.reply_to(message, f"Error: {e}")
    else:
        pass  # Ignore if someone else tries to use /replace

# Handle the /start command
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, f"Greetings, {message.from_user.first_name}! {INTRODUCTION}")

# Respond to user messages
@bot.message_handler(func=lambda message: True)
def chat_response(message):
    user_input = message.text.lower()

    # Check if the user input matches predefined knowledge
    if user_input in KNOWLEDGE_RESPONSES:
        response = random.choice(KNOWLEDGE_RESPONSES[user_input])  # Random answer
    else:
        # Respond with a random generic response
        response = "Hmph, that's a trivial question for someone like me."

    bot.reply_to(message, response)

# Long polling to keep the bot running
bot.polling()
