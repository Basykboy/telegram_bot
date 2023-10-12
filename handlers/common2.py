from aiogram.filters.state import StateFilter
from aiogram.filters.command import Command,Message
from aiogram import Router,F 
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from states import DeleteCommon
router=Router()
@router.message(Command("delete"),StateFilter(None))
async def cmd_delete(message:Message,state:FSMContext):
    kb=[]
    kb.append([InlineKeyboardButton(text="Выбрать ссылку",switch_inline_query_current_chat="links")])
    kb.append([InlineKeyboardButton(text="Выбрать изображение",switch_inline_query_current_chat="images")])
    await state.set_state(DeleteCommon.waiting_for_delete_start)
    await message.answer(text="Выберите, что хотите удалить:", reply_markup=InlineKeyboardMarkup(inline_keyboard=kb))