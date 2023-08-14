from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN_API 
from strings import HELP_COMMAND, START_TEXT, DESCRIPTION, COUNT_ERROR
from backend.main import result
from backend.additional_functions import find_all_names
import logging
#from os import getenv

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

""" КЛАВИАТУРА """
kb = ReplyKeyboardMarkup(resize_keyboard=True) # parameter one_time_keyboard def=False
btn1 = KeyboardButton('Описание')
btn2 = KeyboardButton('Помощь')
kb.add(btn1).add(btn2) # insert(кнопка) - для нов столбика 

ikb = InlineKeyboardMarkup()
ibtn_names_tobacco = InlineKeyboardButton(text="Табаки", callback_data="names_tobacco")
ibtn_back = InlineKeyboardButton(text="Назад", callback_data="back_button")
ikb.add(ibtn_names_tobacco).add(ibtn_back)
""" КОНЕЦ КЛАВИАТУРА """

#Всякие переменные 
count = 0
number_of_inputs = 0
previous_message = ''# Переменная для хранения предыдущего сообщения
#Конец всяких переменных
async def on_startup(_):
    print("Стартуем!")

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    global previous_message
    await message.answer(text= START_TEXT, parse_mode="HTML", reply_markup = ikb) # написать
    previous_message = message.text
    await message.delete() # удоли сообщение пользователя
        
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    global previous_message
    await message.answer(HELP_COMMAND) # ответить
    previous_message = message.text
    await message.delete()
@dp.message_handler(text = 'Помощь')
async def help_command(message: types.Message):
    global previous_message
    await message.answer(HELP_COMMAND) # ответить
    previous_message = message.text
    await message.delete()
        
@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    global previous_message 
    await message.answer(DESCRIPTION)
    previous_message = message.text
    await message.delete()
@dp.message_handler(text = 'Описание')
async def help_command(message: types.Message):
    await message.answer(DESCRIPTION) # ответить
    await message.delete()     

@dp.message_handler(text = 'Пенис')
async def sticker_giver(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEJ9exk0oa87s2dqdLDTO0j6_g3tyYDbgAC1AsAAg74eUlJg1T3YVm93jAE")
   

@dp.message_handler(commands=['photo'])
async def send_penis(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://cdn-icons-png.flaticon.com/512/6147/6147668.png")
    

@dp.message_handler()
async def interception(message: types.Message):
    global number_of_inputs
    global previous_message
    if message.text.count(' ') >= 1:
        previous_message = message.text
        await message.answer(result(message.text), reply_markup= ikb)
    else:
        await message.answer(text = COUNT_ERROR, parse_mode="HTML")
        number_of_inputs +=1
        if number_of_inputs > 2:
            await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEJ9exk0oa87s2dqdLDTO0j6_g3tyYDbgAC1AsAAg74eUlJg1T3YVm93jAE")
            number_of_inputs = 0
          

@dp.callback_query_handler(lambda callback_query: callback_query.data == 'names_tobacco')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text= find_all_names())
    

@dp.callback_query_handler(text='back_button')
async def back_button_handler(query: types.CallbackQuery):
    global previous_message

    # Отправляем предыдущее сообщение
    if previous_message:
        await query.message.bot.send_message(query.from_user.id, previous_message)
        previous_message = ''

    # Удаляем кнопку
    await query.message.delete()    

if __name__ == "__main__":
    #logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
