import telebot
import random
import requests
from pytube import YouTube  # Install with `pip install pytube`

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

# Add multiple answers for the same question using /burger
@bot.message_handler(commands=["burger"])
def learn_new_response(message):
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

# Remove a question and all its answers using /remove
@bot.message_handler(commands=["remove"])
def remove_question(message):
    try:
        question = message.text[8:].strip().lower()  # Extract text after /remove
        if question in KNOWLEDGE_RESPONSES:
            del KNOWLEDGE_RESPONSES[question]
            bot.reply_to(message, f"Removed: Question '{question}' and all its answers.")
        else:
            bot.reply_to(message, f"'{question}' does not exist in my knowledge.")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

# Replace a question and its answers using /replace
@bot.message_handler(commands=["replace"])
def replace_question(message):
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

# Handle the /start command
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, f"Greetings, {message.from_user.first_name}! {INTRODUCTION}")

# Search and download music using YouTube
@bot.message_handler(commands=["music"])
def search_music(message):
    try:
        query = message.text[7:].strip()  # Extract query after /music
        if not query:
            bot.reply_to(message, "Please provide a song name. Example: `/music Shape of You`")
            return

        # Search YouTube for the song
        search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        response = requests.get(search_url)
        if "watch?v=" not in response.text:
            bot.reply_to(message, "Could not find any results for your query.")
            return

        # Extract the first video link
        video_id = response.text.split("watch?v=")[1].split('"')[0]
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        # Reply with the video URL
        bot.reply_to(message, f"Found: {video_url}\nDownloading audio...")

        # Download the audio using pytube
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        file_path = audio_stream.download()

        # Send the audio file to the user
        with open(file_path, "rb") as audio_file:
            bot.send_audio(message.chat.id, audio_file, title=yt.title)
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

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

# Guide command for displaying available commands
@bot.message_handler(commands=["guide"])
def send_guide(message):
    guide_text = (
        "Here are the commands you can use:\n\n"
        "/chat - Chat with me as if I were a real person.\n"
        "/music <song name> - Search for a song, play it, or download it.\n"
    )
    bot.reply_to(message, guide_text)

# Add commands to the bot's menu
def set_bot_commands():
    commands = [
        telebot.types.BotCommand("/guide", "Show available commands"),
    ]
    bot.set_my_commands(commands)

# Set the bot commands at startup
set_bot_commands()

# Long polling to keep the bot running
bot.polling()
