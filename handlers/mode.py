from aiogram import Router,F
from aiogram.types import InlineQuery,InlineQueryResultArticle,InlineQueryResultCachedPhoto,InputTextMessageContent
from storage import get_links_by_id,get_images_by_id
router=Router()
@router.inline_query(F.query=="links")
async def show_user_links(inline_query:InlineQuery):
    results=[]
    def get_message_text():
        for link, link_data in get_links_by_id(inline_query.from_user.id).items():
            results.append(InlineQueryResultArticle(id=link,title=link_data,description=link_data["description"],input_message_content=InputTextMessageContent(message_text=get_message_text(link=link,title=link_data["title"],description=link_data["description"])),parse_mode="HTML"))
    await inline_query.answer(results,is_personal=True)
@router.inline_query(F.query=="images")
async def show_user_images(inline_query:InlineQuery):
    results=[]
    for index, file_id in enumerate(get_images_by_id(inline_query.from_user.id)):
        results.append(InlineQueryResultCachedPhoto(id=str(index),photo_file_id=file_id))
    await inline_query.answer(results,is_personal=True)
