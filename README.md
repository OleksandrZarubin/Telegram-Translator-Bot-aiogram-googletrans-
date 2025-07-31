# Telegram Translator Bot

A simple Telegram bot written in Python using [aiogram 3.x](https://docs.aiogram.dev) and [googletrans](https://pypi.org/project/googletrans/) that translates user text into the selected language.

## 🚀 Features:
- Accepts text messages from users.
- Supports translation commands:
  - `/en` → translate to English.
  - `/ru` → translate to Russian.
  - `/zh-cn` → translate to Simplified Chinese.
- Built-in keyboard for easy language selection.
- Stores the user's last message and translates it upon command.

## 🛠 Technologies:
- Python 3.10+
- aiogram 3.x
- googletrans (unofficial Google Translate API)

## 🔧 How to run:
1. Clone the repository:
   ```bash
   git clone https://github.com/username/telegram-translator-bot.git
   cd telegram-translator-bot
