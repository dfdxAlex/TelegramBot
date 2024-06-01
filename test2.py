import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

API_TOKEN = '6754939943:AAFvmhs3KjuEbz37_BOgbxHWp5kL15x4WBQ'

# Создаем экземпляр бота
bot = Bot(token=API_TOKEN)

# Создаем диспетчер
dp = Dispatcher()

# Обработчик команды /start
# Декоратор привязывается к функции send_welcome() и определяет
# что функцию необходимо запустить тогда, когда будет получена 
# одна из команд. (Магия aiogram)
@dp.message(Command(commands=["start", "aaa"]))
async def send_welcome(message: Message):
    await message.answer("Привет! Я бот, использующий aiogram 3.7.0.")

# Функция для запуска бота
async def main():
    # Пропускаем обновления, накопившиеся во время оффлайна
    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
