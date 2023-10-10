from typing import List
from aiogram import Router, F
from aiogram.types import Message
from filters.find_usernames import HasUsernameFilter
router=Router()
@router.message(F.text,HasUsernameFilter())
async def message_with_usernames(message: Message,usernames:List[str]):
    await message.reply(f"Спасибо! Обязательно подпишусь на "
                        f'{", ".join(usernames)}')