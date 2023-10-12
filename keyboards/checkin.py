from aiogram import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
def get_check_kb()->InlineKeyboardMarkup:
    kb=InlineKeyboardBuilder()
    kb.button(text="Подтвердить",callback_data="confirm")
    return kb.as_markup