from loader import dp, bot
from aiogram import types
from keyboards.inline.menu_data import menuButtons
from aiogram.dispatcher.filters import Command
from states.get_data import GetData
from aiogram.dispatcher.storage import FSMContext
from aiogram.bot import Bot
from middlewares import parser

@dp.callback_query_handler(menuButtons.filter(attribute="reset"))
async def reset(call: types.CallbackQuery, callback_data:dict, state: FSMContext):
    await call.answer(cache_time=30)
    await state.update_data(tags=None)
    await state.update_data(image=None)


@dp.callback_query_handler(menuButtons.filter(attribute="tags"))
async def show_tags(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=30)
    await call.message.answer("Enter 1-5 tags separated by comma  (for example hair color)")
    await GetData.tags_state.set()

@dp.message_handler(state=GetData.tags_state)
async def tags_answer(message: types.Message, state: FSMContext):
    tags = message.text
    await state.update_data(tags=tags)
    await message.answer(f"Your tags - {tags}")
    await state.reset_state(with_data=False)

@dp.callback_query_handler(menuButtons.filter(attribute="image"))
async def show_tags(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=30)
    await call.message.answer("Send preview of video")
    await GetData.image_state.set()

@dp.message_handler(state=GetData.image_state, content_types=types.ContentTypes.PHOTO)
async def tags_answer(message: types.Message, state: FSMContext):
    imageid = message.photo[-1].file_id
    await state.update_data(image_id=imageid)
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=imageid,
                         caption="Got it")
    await state.reset_state(with_data=False)
