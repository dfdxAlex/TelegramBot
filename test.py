# Токен, идентификатор бота, по нему api определяет с 
# каким ботом работать amator4DedBot
TOKEN = '6754939943:AAFvmhs3KjuEbz37_BOgbxHWp5kL15x4WBQ'

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

# Создание объекта бота из класса Bot
bot = Bot(token = TOKEN)

# Создание диспетчера, объекта класса диспечер
dp = Dispatcher(bot)

# bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
# dp = Dispatcher()
# dp.middleware.setup(LoggingMiddleware())


# Зарегестрирован декоратор на команду /start
@dp.message_handler(commands=['start'])
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, введена команда /start")


# @dp.message()
# async def echo_handler(message: Message) -> None:
#     """
#     Handler will forward receive a message back to the sender

#     By default, message handler will handle all message types (like a text, photo, sticker etc.)
#     """
#     try:
#         # Send a copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")


# async def main() -> None:
#     # Initialize Bot instance with default bot properties which will be passed to all API calls
#     bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
#     # And the run events dispatching
#     await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    # asyncio.run(main())

