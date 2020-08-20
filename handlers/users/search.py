from loader import dp, bot
from aiogram import types
from keyboards.inline.menu_data import menuButtons
from states.get_data import GetData
from aiogram.dispatcher.storage import FSMContext
from aiogram.bot import Bot
from middlewares import parser
from io import BytesIO
from aiogram.utils.markdown import hlink


@dp.callback_query_handler(menuButtons.filter(attribute="search"))
async def search(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    data = await state.get_data()
    image_id = data.get("image_id")
    tags = data.get("tags")
    if image_id and tags:
        tags = tags.split(",")[:4]
        tags = list(map(lambda x: x[:10], tags))
        img = await bot.get_file(file_id=image_id)
        image: BytesIO = await bot.download_file(img.file_path)
        await GetData.search_state.set()
        await call.message.answer("Search... wait")
        urls = parser.main(image, tags)
        links = []
        for i in range(len(urls[1])):
            links.append(hlink(urls[0][i], urls[1][i]))
        await call.answer(cache_time=30)
        await call.message.answer("\n".join(links), parse_mode=types.ParseMode.HTML)
        await state.reset_state()
        await state.update_data(tags=None)
        await state.update_data(image=None)
    else:
        await call.message.answer("Not enough data")
