from aiogram import Router
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import Message
from aiogram.filters import Command
from filters.chat_type import ChatTypeFilter
router=Router()
@router.message(ChatTypeFilter(chat_type=["group","supergroup"]),Command(commands=["dice"]))
async def cmd_dice_in_group(message:Message):
    await message.answer_dice(emoji=DiceEmoji.Dice)
@router.message(ChatTypeFilter(chat_type=["group","supergroup"]),Command(commands=["basketball"]))
async def cmd_basketball_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.BASKETBALL)
@router.message(ChatTypeFilter(chat_type=["group","supergroup"]),Command(commands=["bowling"]))
async def cmd_bowling_in_group(message:Message):
    await message.answer_dice(emoji=DiceEmoji.BOWLING)
@router.message(ChatTypeFilter(chat_type=["group","supergroup"]),Command(commands=["dart"]))
async def cmd_dart_in_group(message:Message):
    await message.answer_dice(emoji=DiceEmoji.DART)
@router.message(ChatTypeFilter(chat_type=["group","supergroup"]),Command(commands=["football"]))
async def cmd_football_in_group(message:Message):
    await message.answer_dice(emoji=DiceEmoji.FOOTBALL)
@router.message(ChatTypeFilter(chat_type=["group","supergroup"]),Command(commands=["kazino"]))
async def cmd_kazino_in_group(message:Message):
    await message.answer_dice(emoji=DiceEmoji.SLOT_MACHINE)



