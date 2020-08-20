from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .menu_data import menuButtons
from states.get_data import GetData

menu = InlineKeyboardMarkup(row_width=2,
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(
                                        text="Import tags",
                                        callback_data=menuButtons.new("tags")
                                    ),
                                    InlineKeyboardButton(
                                        text="Import image",
                                        callback_data=menuButtons.new("image")
                                    ),
                                    InlineKeyboardButton(
                                        text="Reset settings",
                                        callback_data=menuButtons.new("reset")
                                    ),
                                    InlineKeyboardButton(
                                        text="Search",
                                        callback_data=menuButtons.new("search")
                                    )
                                ]
                            ])