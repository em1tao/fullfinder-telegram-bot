from aiogram.dispatcher.filters.state import StatesGroup, State


class GetData(StatesGroup):
    """States for getting data."""
    tags_state = State()
    image_state = State()
    search_state = State()
