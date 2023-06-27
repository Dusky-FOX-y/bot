from aiogram.types import Message
from loader import dp
from states.UserStates import UserState
from aiogram.types import ContentType, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types.web_app_info import WebAppInfo
import json
from utils import req

# Sending messages with info about orders


@dp.message_handler(commands=['order'], state='*')
async def orders(message: Message):
    if req.check(message.from_user.id):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        button = KeyboardButton("Оформить заказ", web_app=WebAppInfo(url="https://dusky-fox-y.github.io/MiniSite/"))
        keyboard.add(button)
        await message.answer("Вот кнопочка для отправки заказа", reply_markup=keyboard)
    else:
        await message.answer("Ой кажется вы ещё не прошли регистрацию")


@dp.message_handler(content_types=["web_app_data"])
async def web_data(message: Message):
    keyboard = ReplyKeyboardRemove()
    asd = message.web_app_data.data.replace('\\', "")
    asd = asd.replace('"[', '[')
    asd = asd.replace(']"', ']')
    asd = json.loads(asd)
    mess = req.add_order(asd, message.from_user.id)
    await message.answer(f"Данные получены! Ваш заказ:\n{mess}", reply_markup=keyboard)
