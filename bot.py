import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random
import os
import logging
import time
from flask import Flask
import threading

# ===== Setup ===== #
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN, parse_mode="MarkdownV2")
logging.basicConfig(level=logging.INFO)

# ===== Flask Server (Required for Render) ===== #
app = Flask(__name__)

@app.route('/')
def health_check():
    return "✅ LifeBoost Bot is running!", 200

# ===== Advice Library ===== #
ADVICE_LIBRARY = {
    "🚀 Productivity": [
        r"*2\-minute rule*: If a task takes \<2 minutes\, do it NOW",
        r"*Plan your day* the night before\! Waking up with a plan boosts efficiency",
        r"*Single\-tasking \> multitasking*: Focus on one thing until completion",
        r"Use the *Pomodoro technique*: 25 min work → 5 min break",
        r"*Batch similar tasks* \(emails\, calls\) to reduce mental switching costs"
    ],
    "💪 Confidence": [
        r"*Stand tall* for 2 minutes: Power poses boost confidence hormones",
        r"Keep a *win journal*: Write 3 daily victories\, no matter how small",
        r"*Speak 10\% slower*: Projects authority and gives you time to think",
        r"Dress like the *2\.0 version* of yourself",
        r"*Fail forward*: Every mistake is data for improvement"
    ],
    "❤️ Relationships": [
        r"*Listen 2x more* than you speak: People remember how you made them feel",
        r'*Give specific compliments*: "You handled that situation gracefully" > "Good job"',
        r"*Assume positive intent*: Most people aren't trying to annoy you",
        r"*Check in* with important people at least monthly",
        r'*Be vulnerably honest*: "I messed up" builds more trust than perfect excuses'
    ],
    "🧠 Mindset": [
        r'*Reframe challenges*: "What can I learn from this\?" vs "Why me\?"',
        r"*Gratitude journal* daily: Write 3 things you're thankful for",
        r"*Compare yourself* only to who you were yesterday",
        r"*Meditate 5 minutes* daily: Reduces anxiety significantly",
        r"*Read biographies*: Learn from others' life lessons"
    ],
    "🎲 Random": [
        r"*Energy flows where attention goes*: Focus on solutions\, not problems",
        r"*Done is better than perfect*: Launch then improve",
        r"*You're the average* of the 5 people you spend the most time with",
        r"*Start before you're ready*: 70\% prepared is enough",
        r"*If it won't matter* in 5 years\, don't spend 5 days worrying"
    ]
}

# ===== Keyboard ===== #
def create_main_keyboard():
    markup = ReplyKeyboardMarkup(
        row_width=2, 
        resize_keyboard=True, 
        one_time_keyboard=False
    )
    buttons = [KeyboardButton(category) for category in ADVICE_LIBRARY.keys()]
    markup.add(*buttons)
    return markup

# ===== Message Handlers ===== #
@bot.message_handler(commands=['start', 'help', 'advice'])
def send_welcome(message):
    welcome_msg = r"""
*🌟 Welcome to LifeBoost Bot\!* 
Get instant life advice in these categories\:
"""
    bot.send_message(
        message.chat.id,
        welcome_msg,
        reply_markup=create_main_keyboard()
    )

@bot.message_handler(func=lambda msg: msg.text in ADVICE_LIBRARY)
def send_advice(message):
    try:
        category = message.text
        advice = random.choice(ADVICE_LIBRARY[category])
        bot.send_message(message.chat.id, advice)
        logging.info(f"Sent {category} advice to {message.from_user.id}")
    except Exception as e:
        logging.error(f"Error: {e}")
        bot.reply_to(message, "⚠️ Couldn't fetch advice. Try again later.")

@bot.message_handler(func=lambda msg: True)
def handle_unknown(message):
    bot.send_message(
        message.chat.id,
        "Please select a category from the buttons below 👇",
        reply_markup=create_main_keyboard()
    )

# ===== Deployment Setup ===== #
if __name__ == "__main__":
    # Clean previous connections
    bot.remove_webhook()
    time.sleep(1)
    
    # Start bot in background thread
    bot_thread = threading.Thread(
        target=bot.infinity_polling,
        daemon=True
    )
    bot_thread.start()
    logging.info("🤖 Bot started in background thread")
    
    # Start Flask server (required for Render)
    logging.info("🌐 Starting Flask server on port 8000")
    app.run(host='0.0.0.0', port=8000)
