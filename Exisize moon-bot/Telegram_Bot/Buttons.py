from aiogram.types import InlineKeyboardMarkup, \
    InlineKeyboardButton, ReplyKeyboardMarkup


def main():
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.add(InlineKeyboardButton(text='Ввести значения', callback_data='start'))
    markup.add(InlineKeyboardButton(text='Стандартные значения', callback_data='default'))
    return markup


def set_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text="Меркурий", callback_data="planet_mercury"),
            InlineKeyboardButton(text="Венера", callback_data="planet_venus"),
            InlineKeyboardButton(text="Солнце", callback_data="planet_sun")
        ],
        [
            InlineKeyboardButton(text="Марс", callback_data="planet_mars"),
            InlineKeyboardButton(text="Юпитер", callback_data="planet_jupiter"),
            InlineKeyboardButton(text="Сатурн", callback_data="planet_saturn")
        ],
        [
            InlineKeyboardButton(text="Уран", callback_data="planet_uranus"),
            InlineKeyboardButton(text="Нептун", callback_data="planet_neptune"),
            InlineKeyboardButton(text="Плутон", callback_data="planet_pluto")
                ],
        [
            InlineKeyboardButton(text="Луна", callback_data="planet_moon"),
            InlineKeyboardButton(text="Земля", callback_data="planet_earth"),
        ]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def cancel():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(InlineKeyboardButton(text='Отмена'))
    return markup


def values():
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.add(InlineKeyboardButton(text='Ввести значения', callback_data='start'))
    return markup


def cancel_inl():
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.add(InlineKeyboardButton(text='Отмена!', callback_data='cancel'))
    return markup
