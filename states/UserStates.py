from aiogram.dispatcher.filters.state import State, StatesGroup


class UserState(StatesGroup):
    reg_phone = State()
    reg_adress = State()
    