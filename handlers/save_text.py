from typing import Optional

from aiogram import Router, F
from aiogram.filters.command import Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from filters import HasLinkFilter
from states import SaveCommon, TextSave
from storage import add_link

router = Router()

@router.message(F.text,SaveCommon.waiting_for_save_start,HasLinkFilter())
async def save_text_has_link(message: Message, link: str, state: FSMContext):
    await state.update_data(link=link)
    await state.set_state(TextSave.waiting_for_title)
    await message.answer(
        text=f"Окей, я нашёл в сообщении ссылку {link}. "
             f"Теперь отправь мне описание (не больше 30 символов)"
    )

@router.message( F.text,SaveCommon.waiting_for_save_start)
async def save_text_no_link(message: Message):
    await message.answer(
        text="Эмм.. я не нашёл в твоём сообщении ссылку. "
             "Попробуй ещё раз или нажми /cancel, чтобы отменить."
    )

@router.message(F.text.func(len) <= 30,TextSave.waiting_for_title, )
async def title_entered_ok(message: Message, state: FSMContext):
    await state.update_data(title=message.text, description=None)
    await state.set_state(TextSave.waiting_for_description)
    await message.answer(
        text="Так, заголовок вижу. Теперь введи описание "
             "(тоже не больше 30 символов) "
             "или нажми /skip, чтобы пропустить этот шаг"
    )

@router.message(F.text.func(len) <= 30,TextSave.waiting_for_description, )
@router.message(TextSave.waiting_for_description, Command("skip"))
async def last_step(
        message: Message,
        state: FSMContext,
        command: Optional[CommandObject] = None
):
    if not command:
        await state.update_data(description=message.text)
    # Сохраняем данные в нашу ненастоящую БД
    data = await state.get_data()
    add_link(message.from_user.id, data["link"], data["title"], data["description"])
    await state.clear()
    kb = [[InlineKeyboardButton(
        text="Попробовать",
        switch_inline_query="links"
    )]]
    await message.answer(
        text="Ссылка сохранена!",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=kb)
    )

@router.message(F.text,TextSave.waiting_for_title)
@router.message(F.text,TextSave.waiting_for_description)
async def text_too_long(message: Message):
    await message.answer("Слишком длинный заголовок. Попробуй ещё раз")
    return