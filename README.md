# 🌟 WEHEL BOT- Your Pocket Motivational Coach

[![Deploy on Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)
[![Telegram Bot](https://img.shields.io/badge/💬_Try_It-Telegram-blue?logo=telegram)](https://t.me/kacabdev_bot)

> Instant life advice at your fingertips - powered by Python and positivity

## ✨ Features

- **25+ curated wisdom nuggets** across 5 categories
- **One-tap interaction** with smart reply keyboards  
- **Markdown-rich formatting** for optimal readability
- **24/7 reliable hosting** on Render
- **Crash-resistant** architecture with auto-recovery

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Telegram bot token ([@BotFather](https://t.me/BotFather))
- Render account (free tier available)

### Local Development
```bash
# 1. Clone repository
git clone https://github.com/yourusername/lifeboost-bot.git
cd lifeboost-bot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
echo "TELEGRAM_BOT_TOKEN=your_token_here" > .env

# 4. Launch bot
python bot.py


## 🛠️ Tech Stack

| Component       | Technology Used   | Purpose                          |
|-----------------|-------------------|----------------------------------|
| Core Framework  | Python 3.10       | Backend logic and execution      |
| Telegram API    | pyTelegramBotAPI  | Handles bot communication        |
| Web Server      | Flask             | Provides health checks for Render|
| Configuration   | python-dotenv     | Secures environment variables    |
| Error Handling  | Python logging    | Tracks and reports bot crashes   |



# 1. Resilient bot launch
threading.Thread(
    target=bot.infinity_polling,
    daemon=True
).start()

# 2. Advice database
ADVICE_LIBRARY = {
    "🚀 Productivity": [
        "2-minute rule: If a task takes <2 mins, do it NOW",
        # ... 25+ more gems ...
    ]
}

# 3. Interactive keyboard
def create_main_keyboard():
    return ReplyKeyboardMarkup(
        row_width=2,
        resize_keyboard=True
    )



🚀 Deployment Guide
Set up on Render:

Connect your GitHub repo

Add TELEGRAM_BOT_TOKEN environment variable

Set start command: python bot.py

Verify deployment:

Check logs for Bot started in background thread

Visit your Render URL to see "✅ Bot is running!"

🤝 Contributing
We welcome improvements! Here's how:

Fork the repository

Create a feature branch (git checkout -b feature/your-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/your-feature)

Open a Pull Request

📜 License
MIT License - Free for personal and commercial use
