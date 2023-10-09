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
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
# Диспетчер
dp = Dispatcher()
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
@dp.message(F.sticker)
async def echo_smile(message:types.Message):
    await message.reply_sticker(message.sticker.file_id)
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
@dp.message(Command("hidden_link"))
async def cmd_hidden_link(message: types.Message):
    await message.answer(
        f"{hide_link('https://telegra.ph/file/562a512448876923e28c3.png')}"
        f"Документация Telegram: *существует*\n"
        f"Пользователи: *не читают документацию*\n"
        f"Груша:"
    )
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb=[
        [
        types.KeyboardButton(text="Пампарам"),
        types.KeyboardButton(text="Изи изи изи для папизи")
        ]
    ]
    keyboard=types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Что говорит папич", reply_markup=keyboard)  
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    