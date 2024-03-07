from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

first_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Получить информацию по товару'), KeyboardButton(text='Остановить уведомления')],
    [KeyboardButton(text='Получить информацию из БД')]
],
    resize_keyboard=True,
    # one_time_keyboard=True,
    input_field_placeholder='Выбери команду')

follow = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Подписаться на товар', callback_data='follow')]
])