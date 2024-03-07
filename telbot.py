from dotenv import load_dotenv
import os
import asyncio
import logging


from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import keyboards as kb
from scripts import get_info
from dbcore import insert_history, insert_subscribers, select_subscribers, select_history, delete_subscriber


load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


class Product(StatesGroup):
    prod_id = State()


@dp.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Добрый день, выбери пункт меню, нажав на кнопку',
                         reply_markup=kb.first_keyboard)


@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Тут помощь \nЕщё есть \n/start и \n/help')


@dp.message(F.text == 'Получить информацию по товару')
async def get_good_number(message: Message, state: FSMContext):
    await state.set_state(Product.prod_id)
    await message.answer('Введи код товара')


@dp.message(Product.prod_id)
async def get_good_info(message: Message, state: FSMContext):
    try:
        user_id = message.from_user.id
        good_info = get_info(int(message.text))
        await state.update_data(prod_id=message.text)
        data = await state.get_data()
        insert_history(user_id, good_info["article"])
        await message.answer(f'Товар {good_info["prod_name"]}\n'
                             f'Артикул {good_info["article"]}\n'
                             f'Цена {good_info["price"]} руб.\n'
                             f'Всего остатки на складах {good_info["quantity"]}\n',
                             reply_markup=kb.follow)
    except Exception:
        await message.answer('Нет такого товара')


@dp.callback_query(F.data == 'follow')
async def make_follow(callback: CallbackQuery, state: FSMContext):
    id = callback.from_user.id
    data = await state.get_data()
    insert_subscribers(id, int(data['prod_id']))
    await callback.answer('Подпискка оформлена')
    await state.clear()
    # await callback.message.answer('Вы успешно подписались')


@dp.message(F.text == 'Остановить уведомления')
async def stop_follow(message: Message):
    id = message.from_user.id
    delete_subscriber(id)
    await message.answer('Уведомления остановлены')


@dp.message(F.text == 'Получить информацию из БД')
async def get_good_info(message: Message):
    bd_info = select_history()
    text = ''
    if bd_info:
        text = f'Вот последние {len(bd_info)} запросов\n'
        for note in bd_info:
            text += f"{note[2].strftime('%d.%m.%y %H:%M')} пользователь с id{note[1]}, запрашивал информацию по товару {note[3]}\n"
    else:
        text = 'Запросов к базе не было'
    await message.answer(text)


@dp.message(F.text)
async def get_good_info(message: Message):
    await message.answer('Неверная команда')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except Exception as e:
        print(e)