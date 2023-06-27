from aiogram.types import Message
from loader import dp
from states.UserStates import UserState
from aiogram.types import ContentType
# from utils import checker as sc
from utils import req

@dp.message_handler(commands=['test'], state='*')
async def orders(message: Message):
    print(message.from_user)
    # req.reg_new_acc(message.from_user.id)
    await message.answer("Соси")
    pass
