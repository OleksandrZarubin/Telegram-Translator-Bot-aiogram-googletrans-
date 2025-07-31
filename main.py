from aiogram import Bot, Dispatcher
import asyncio
from handlers import router

token = ""


async def main():
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
    print("Bot is on!")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is off")
