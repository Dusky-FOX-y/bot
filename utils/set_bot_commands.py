from aiogram.types import BotCommand


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        
        # TODO

        BotCommand(
            "start",
            "Зарегистрироваться"
        ),

        #TODO

        BotCommand(
            "order",
            "Создать заказ"
        )
    ])
