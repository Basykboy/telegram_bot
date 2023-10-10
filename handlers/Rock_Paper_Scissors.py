from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import types,F
import random
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from filters.chat_type import ChatTypeFilter

router=Router()
spisok=["Камень","Ножницы","Бумага"]
@router.message(ChatTypeFilter(chat_type=["private","supergroup"]),Command(commands=["rock_paper_scissors"]))
async def cmd_rock_paper_scissors(message: types.Message):
    kb=[
        [
        (types.KeyboardButton(text="Камень")),
        (types.KeyboardButton(text="Ножницы")),
        (types.KeyboardButton(text="Бумага")),
        (types.KeyboardButton(text="Выход"))
        ]
    ]
    keyboard=types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Играть в камень ножницы бумага", reply_markup=keyboard)
@router.message(F.text.lower() == "выход")
async def exit(message:types.Message):
    await message.reply("Вышли из игры", reply_markup=types.ReplyKeyboardRemove())
@router.message(F.text.lower() == "камень")
async def rock_paper_scissors(message: types.Message):
    move=random.choice(spisok)
    if move == "Бумага":
        await message.reply("Я победил")
    elif move == "Ножницы":
        await message.reply("Ты победил")
    elif move == "Камень":
        await message.reply("Ничья")
@router.message(F.text.lower() == "ножницы")
async def rock_paper_scissors(message: types.Message):
    move=random.choice(spisok)
    if move == "Бумага":
        await message.reply("Я проиграл")
    elif move == "Ножницы":
        await message.reply("Ничья")
    elif move == "Камень":
        await message.reply("Я победил")
@router.message(F.text.lower() == "бумага")
async def rock_paper_scissors(message: types.Message):
    move=random.choice(spisok)
    if move == "Бумага":
        await message.reply("Ничья")
    elif move == "Ножницы":
        await message.reply("Я победил")
    elif move == "Камень":
        await message.reply("Я проиграл")