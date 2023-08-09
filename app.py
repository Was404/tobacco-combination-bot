from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import TOKEN_API 
from strings import HELP_COMMAND, START_TEXT, DESCRIPTION

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

""" КЛАВИАТУРА """
kb = ReplyKeyboardMarkup(resize_keyboard=True) # parameter one_time_keyboard def=False
btn1 = KeyboardButton('/give')
btn2 = KeyboardButton('/count')
kb.add(btn1).add(btn2) # insert(кнопка) - для нов столбика 
""" КОНЕЦ КЛАВИАТУРА """

count = 0

async def on_startup(_):
    print("Стартуем!")

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text= START_TEXT, parse_mode="HTML", reply_markup=kb) # написать
    await message.delete() # удоли сообщение пользователя
        
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(HELP_COMMAND) # ответить

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer(DESCRIPTION)
    await message.delete()

@dp.message_handler(commands=['count'])
async def check_count(message: types.Message):
    global count
    await message.answer(f'COUNT: {count}')
    count += 1

@dp.message_handler()
async def check_penis(message: types.Message):
    if 'Пенис' or 'пенис' in message.text:
        await message.reply('YES')

@dp.message_handler(commands=['give'])
async def sticker_giver(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEJ9exk0oa87s2dqdLDTO0j6_g3tyYDbgAC1AsAAg74eUlJg1T3YVm93jAE")
    await message.delete()

@dp.message_handler()
async def emoji_giver(message: types.Message):
    await message.reply(message.text + '💋 ')

@dp.message_handler(commands=['photo'])
async def send_penis(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://cdn-icons-png.flaticon.com/512/6147/6147668.png")
    await message.delete()

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
