from aiogram import Bot, Dispatcher
import asyncio
from handlers import router
import os


TOKEN = os.getenv("BOT_TOKEN")

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
    print("Bot is on!")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is off")
