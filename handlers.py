from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from keyboard import keyboard


from googletrans import Translator

router = Router()
translater = Translator()
user_message = None


@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer("Hi\n\nI am a bot that can translate your text into any language I suggest", reply_markup=keyboard)


@router.message(Command("en"))
async def cmd_en(message:Message):
    global user_message
    translated = translater.translate(user_message, dest="en")
    await message.answer(translated.text)


@router.message(Command("ru"))
async def cmd_en(message:Message):
    global user_message
    translated = translater.translate(user_message, dest="ru")
    await message.answer(translated.text)


@router.message(Command("zh-cn"))
async def cmd_en(message:Message):
    global user_message
    translated = translater.translate(user_message, dest="zh-cn")
    await message.answer(translated.text)


@router.message(F.text & ~F.text.startswith("/"))
def handle_message(message: types.Message):
    global user_message
    user_message = message.text







