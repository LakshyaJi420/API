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

# Predefined responses
KNOWLEDGE_RESPONSES = {
    "what is your name": "I am Kirmada, the eternal and all-powerful.",
    "who are you": INTRODUCTION,
    "how old are you": "I am ageless, immortal, and eternal.",
    "what is the capital of india": "The capital of India is New Delhi.",
    "what is 2+2": "That's easy, it's 4. Even mortals know that.",
    "what is gravity": "Gravity is a force that pulls objects toward each other. I, of course, am beyond its grasp.",
    "what is your hobby": "My hobby is contemplating the infinite and laughing at the limits of mortals.",
}

# Catch-all phrases for unrecognized inputs
CATCH_ALL_RESPONSES = [
    "Hmph, that's a trivial question for someone like me.",
    "Interesting... why don't you tell me more?",
    "I am far too wise to waste time on such questions.",
    "Speak clearly, mortal, so I can comprehend your curiosity.",
    "Why would you ask me that? Have you no better questions?",
]

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
        response = KNOWLEDGE_RESPONSES[user_input]
    else:
        # Respond with a random generic response
        response = random.choice(CATCH_ALL_RESPONSES)

    bot.reply_to(message, response)

# Long polling to keep the bot running
bot.polling()
