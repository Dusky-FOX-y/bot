from aiogram.types import Message
from loader import dp
from states.UserStates import UserState
from aiogram.types import ContentType
from utils import req

@dp.message_handler(commands=['start'], state='*')
async def start(message: Message):
    try:
        name = message.from_user.full_name
    except Exception:
        pass
    try:
        username = message.from_user.username
    except Exception:
        pass

    if req.reg_new_acc(message.from_user.id, name=name,nickname=username):
        await message.answer("Привет мой друг, давай знакомится, укажи свой номер телефона")
        await UserState.reg_phone.set()
    else:
        if req.check(message.from_user.id):
            await message.answer("Ой, что-то пошло не так, скоре всего ты уже зарегистрирован")
        else:
            await message.answer("Ой, как-то так получилось, что ты не указал свои контакные данные,укажи свой номер телефона") 
            await UserState.reg_phone.set()

@dp.message_handler(content_types=ContentType.TEXT, state=UserState.reg_phone)
async def reg_phone(message: Message):
    if len(message.text) > 12:
        await message.answer("Кажется это вообще не номер телефона, давай по новой")
        return
    if req.update_acc(message.from_user.id, field="phone", value=message.text):
        await message.answer("Замечательно, давай дальше. Укажи свой адрес")
        await UserState.reg_adress.set()
    else:
        await message.answer("Ой, что-то пошло не так")


@dp.message_handler(content_types=ContentType.TEXT, state=UserState.reg_adress)
async def reg_adress(message: Message, state):
    if req.update_acc(message.from_user.id, field="address", value=message.text):
        req.update_acc(message.from_user.id, field="permissions", value=1)
        await message.answer("Поздравляю, ты успешно зарегистрирован!")
        await state.finish()
    else:
        await message.answer("Ой, что-то пошло не так")
