from aiogram.types import Message
from loader import dp
from states.UserStates import UserState
from aiogram.types import ContentType
from utils import checker as sc
from utils import req

@dp.message_handler(commands=['test'], state='*')
async def orders(message: Message):
    asd = message.text.split(" ")
    if req.add_good(asd[1], asd[2]):
        await message.answer("Good succesfully added")
    else:
        await message.answer("Some issues handled")
