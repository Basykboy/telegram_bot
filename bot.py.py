from config_reader import config
import asyncio
import logging
from aiogram import Bot, Dispatcher,types
from aiogram.filters.command import Command
from aiogram import types
from aiogram.filters import Command
from aiogram.filters import CommandObject
from aiogram import html
from datetime import datetime
from aiogram import F
from aiogram.utils.markdown import hide_link
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
import random
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from typing import Optional
from aiogram.filters.callback_data import CallbackData
from magic_filter import F
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from aiogram.utils.callback_answer import CallbackAnswer
from handlers import group_games,usernames,Rock_Paper_Scissors
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
# Диспетчер
dp = Dispatcher()
dp.include_routers(usernames.router,group_games.router,Rock_Paper_Scissors.router)
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer("Hello!")
# Хэндлер на команду /test1
@dp.message(Command("answer"))
async def cmd_answer(message: types.Message):
    await message.answer("Написал сообщение")

# Хэндлер на команду /test2
@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply("Ответил на сообщения")
    dp.message.register(cmd_reply, Command("test2"))
@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")
@dp.message(Command("test"))
async def any_message(message: types.Message):
    await message.answer("Hello, <b>world</b>!", parse_mode="HTML")
    await message.answer("Hello, *world*\!", parse_mode="MarkdownV2")
@dp.message(Command("name"))
async  def cmd_name(message: types.Message, command:CommandObject):
    if command.args:
        await message.answer(f"Привет, {html.bold(html.quote(command.args))}")
    else:
        await message.answer("Пожалуйста, укажи своё имя после команды /name")
# @dp.message(F.text)
# async def echo_with_time(message: types.Message):
#     time_now=datetime.now().strftime('%H:%M')
#     added_text=html.underline(f"Создано в {time_now}")
#     await message.answer(f"{message.html_text}\n\n{added_text}", parse_mode="HTML")
# @dp.message(F.text)
# async def extract_data(message: types.Message):
#     data={
#         "url":"<N/A>",
#         "email":"<N/A>",
#         "code":"<N/A>"
#     }
#     entities=message.entities or []
#     for item in entities:
#         if item.type in data.keys():
#             # Неправильно
#             # data[item.type] = message.text[item.offset : item.offset+item.length]
#             #Правильно
#             data[item.type]=item.extract_from(message.text)
#     await message.reply(
#         "Вот что я нашёл:\n"
#         f"URL:{html.quote(data['url'])}\n"
#         f"Email:{html.quote(data['email'])}"
#         f"Пароль:{html.quote(data['code'])}"
#     )
# @dp.message(F.sticker)
# async def echo_smile(message:types.Message):
#     await message.reply_sticker(message.sticker.file_id)
# @dp.message(Command("images"))
# async def upload_photo(message:types.Message):
#     file_ids=[]
#     with open("sniper.png","rb") as image_from_buffer:
#         result=await message.answer_photo(
#         BufferedInputFile(image_from_buffer.read(),filename="sniper.png"),caption="Изображение из буффера")
#         file_ids.append(result.photo[-1].file_id)
#     image_from_pc=FSInputFile("sniper.png")
#     result=await message.answer_photo(image_from_pc,caption="Изображение из файла на компьютере")
#     file_ids.append(result.photo[-1].file_id)
#     image_from_url=URLInputFile("https://yandex.ru/images/search?text=%D0%A4%D0%9E%D0%A2%D0%9A%D0%90&pos=0&rpt=simage&img_url=https%3A%2F%2Fsteamuserimages-a.akamaihd.net%2Fugc%2F5085158533761058065%2FD572CC315D04FAD42F0331EC379869258927B4B1%2F%3Fimw%3D512%26amp%3Bimh%3D384%26amp%3Bima%3Dfit%26amp%3Bimpolicy%3DLetterbox%26amp%3Bimcolor%3D%2523000000%26amp%3Bletterbox%3Dtrue&from=tabbar&lr=142630")
#     result= await message.answer_photo(image_from_url,caption="Изображение по ссылке")
#     file_ids.append(result.photo[-1].file_id)
#     await message.answer("Отправленные файлы:\n "+"\n".join(file_ids))
# @dp.message(F.photo)
# async def download_photo(message: types.message, bot:Bot):
#     await bot.download(
#         message.photo[-1],
#         destination=f"C:\\Users\\ayrat\\Downloads{message.photo[-1].file_id}.jpg"
#     )
# @dp.message(F.sticker)
# async def download_sticker(message:types.Message, bot:Bot):
#     await bot.download(
#         message.sticker,
#         destination=f"C:\\Users\\ayrat\\Downloads{message.sticker.file_id}.webp"
#     )
# @dp.message(F.new_chat_members)
# async def somebody_added(message: types.Message):
#     for user in message.new_chat_members:
#         await message.reply(f"Привет, {user.full_name}")
# @dp.message(Command("hidden_link"))
# async def cmd_hidden_link(message: types.Message):
#     await message.answer(
#         f"{hide_link('https://telegra.ph/file/562a512448876923e28c3.png')}"
#         f"Документация Telegram: *существует*\n"
#         f"Пользователи: *не читают документацию*\n"
#         f"Груша:"
#     )
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     kb=[
#         [
#         types.KeyboardButton(text="Пампарам"),
#         types.KeyboardButton(text="Изи изи изи для папизи")
#         ]
#     ]
#     keyboard=types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
#     await message.answer("Что говорит папич", reply_markup=keyboard)
# @dp.message(F.text.lower() == "пампарам")
# async def with_puree(message: types.Message):
#     await message.reply("Привет всех смотрящих")

# @dp.message(F.text.lower() == "изи изи изи для папизи")
# async def without_puree(message: types.Message):
#     await message.reply("НАААААААААААА")
# @dp.message(Command("reply_builder"))
# async def reply_builder(message: types.Message):
#     builder = ReplyKeyboardBuilder()
#     for i in range(1, 17):
#         builder.add(types.KeyboardButton(text=str(i)))
#     builder.adjust(4)
#     await message.answer(
#         "Выберите число:",
#         reply_markup=builder.as_markup(resize_keyboard=True),
#     )
    
# @dp.message(Command("special_buttons"))
# async def cmd_special_buttons(message: types.Message):
#     builder = ReplyKeyboardBuilder()
#     builder.row(types.KeyboardButton(text="Запросить геолокацию", request_location=True),types.KeyboardButton(text="Запросить контакт",request_contact=True))
#     builder.row(types.KeyboardButton(text="Создать викторину", request_poll=types.KeyboardButtonPollType(type="quiz")))
#     builder.row(types.KeyboardButton(text="Выбрать премиум пользователя", request_user=types.KeyboardButtonRequestUser(request_id=1,user_is_premium=1)),types.KeyboardButton(text="Выбрать супергруппу с форумами",request_chat=types.KeyboardButtonRequestChat(request_id=2,chat_is_channel=False,chat_is_forum=True)))
#     await message.answer("Выбрать действие:",reply_markup=builder.as_markup(resize_keyboard=True))
# @dp.message(F.user_shared)
# async def on_user_shared(message: types.Message):
#     print(f"Request {message.user_shared.request_id}"
#           f"User ID {message.user_shared.user_id}")
# @dp.message(F.char_shared)
# async def on_user_share(message: types.Message):
#     print(f"Request {message.chat_shared.request_id}"
#           f"Chat ID {message.chat_shared.chat_id}")
# @dp.message(Command("inline_url"))
# async def cmd_inline_url(message: types.Message,bot:Bot):
#     builder = InlineKeyboardBuilder()
#     builder.row(types.InlineKeyboardButton(text="Github",url="https://github.com/dashboard"))
#     builder.row(types.InlineKeyboardButton(text="Оф.канал Telegram",url="tg://resolve?domain=telegram"))
    # user_id=1234567890
    # chat_info=await bot.get_chat(user_id)
    # if not chat_info.has_private_forwards:
    #     builder.row(types.InlineKeyboardButton(text="Какой-то пользователь",url=f"tg://user?id={user_id}"))
    # await message.answer("Выберите ссылку",reply_markup=builder.as_markup())
@dp.message(Command("random"))
async def cmd_random(message : types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await message.answer("Нажмите на кнопку, чтобы бот отправил вам число от 1 до 100",reply_markup=builder.as_markup())
@dp.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer((str(random.randint(1,100))))
    await callback.answer()
userdata={}
# def get_keyboard():
#     buttons=[
#         [
#             types.InlineKeyboardButton(text="-1",callback_data="num_decr"),
#             types.InlineKeyboardButton(text="+1",callback_data="num_incr")
#         ],
#             [types.InlineKeyboardButton(text="Подтвердить",callback_data="num_finish")]
#         ]
#     keyboard=types.InlineKeyboardMarkup(inline_keyboard=buttons)
#     return keyboard
# async def update_num_text(message: types.Message,new_value: int):
#     with suppress(TelegramBadRequest):
#         await message.edit_text(f"Укажите число:{new_value}",reply_markup=get_keyboard())
# @dp.message(Command("numbers"))
# async def cmd_numbers(message: types.Message):
#     userdata[message.from_user.id]=0
#     await message.answer("Укажите число: 0",reply_markup=get_keyboard())
# @dp.callback_query(F.data.startswith("num_"))
# async def callbacks_num(callback:types.CallbackQuery):
#     user_value=userdata.get(callback.from_user.id,0)
#     action=callback.data.split("_")[1]
#     if action == "incr":
#         userdata[callback.from_user.id]=user_value+1
#         await update_num_text(callback.message, user_value+1)
#     elif action == "decr":
#         userdata[callback.from_user.id]=user_value-1
#         await update_num_text(callback.message,user_value-1)
#     elif action=="finish":
#         await callback.message.edit_text(f"Итого: {user_value}")
#     await callback.answer()
class NumbersCallbackFactory(CallbackData,prefix="fabnum"):
    action: str
    value:Optional[int]=None
def get_keyboard_fab():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="-2", callback_data=NumbersCallbackFactory(action="change", value=-2)
    )
    builder.button(
        text="-1", callback_data=NumbersCallbackFactory(action="change", value=-1)
    )
    builder.button(
        text="+1", callback_data=NumbersCallbackFactory(action="change", value=1)
    )
    builder.button(
        text="+2", callback_data=NumbersCallbackFactory(action="change", value=2)
    )
    builder.button(
        text="Подтвердить", callback_data=NumbersCallbackFactory(action="finish")
    )
    # Выравниваем кнопки по 4 в ряд, чтобы получилось 4 + 1
    builder.adjust(4)
    return builder.as_markup()
async def update_num_text_fab(message: types.Message, new_value: int):
    with suppress(TelegramBadRequest):
        await message.edit_text(
            f"Укажите число: {new_value}",
            reply_markup=get_keyboard_fab()
        )

@dp.message(Command("numbers_fab"))
async def cmd_numbers_fab(message: types.Message):
    userdata[message.from_user.id] = 0
    await message.answer("Укажите число: 0", reply_markup=get_keyboard_fab())
@dp.callback_query(NumbersCallbackFactory.filter())
async def callback_num_change_fab(callback:types.CallbackQuery, callback_data:NumbersCallbackFactory):
    user_value=userdata.get(callback.from_user.id,0)
    if callback_data.action == "change":
        userdata[callback.from_user.id]=user_value+callback_data.value
        await update_num_text_fab(callback.message,user_value+callback_data.value)
    else:
        await callback.message.edit_text(f"Итого: {user_value}")
    await callback.answer()
@dp.callback_query(NumbersCallbackFactory.filter())
async def callbacks_num_change_fab(
        callback: types.CallbackQuery, 
        callback_data: NumbersCallbackFactory
):
    # Текущее значение
    user_value = userdata.get(callback.from_user.id, 0)
    # Если число нужно изменить
    if callback_data.action == "change":
        userdata[callback.from_user.id] = user_value + callback_data.value
        await update_num_text_fab(callback.message, user_value + callback_data.value)
    # Если число нужно зафиксировать
    else:
        await callback.message.edit_text(f"Итого: {user_value}")
    await callback.answer()
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    