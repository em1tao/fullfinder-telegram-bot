from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.misc import rate_limit
from keyboards.inline.menu_buttons import menu
from aiogram.dispatcher.storage import FSMContext


from loader import dp

@rate_limit(limit=10)
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    data = await state.get_data()
    tags = data.get("tags")
    if data.get("image_id"):
        image = "✅ Uploaded"
    else:
        image = "🚫 Not uploaded"
    help_message = (f'Hello, {message.from_user.full_name}! I am <b>FullFinder</b> bot.',
                    'I can find video on PornHub by tags and preview.'
                    'Type /start again, for reset settings.',
                    'Write @em1tao for help',
                    f'Tags - {tags}',
                    f'Image - {image}')
    await message.answer("\n ".join(help_message), reply_markup=menu)
