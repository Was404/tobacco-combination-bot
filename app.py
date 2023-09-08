from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from aiogram.dispatcher import FSMContext
from strings import HELP_COMMAND, START_TEXT, DESCRIPTION, COUNT_ERROR
from backend.main import result
from backend.main import handle_variable
from backend.additional_functions import find_all_names, ManufacorChoice, handle_variable2
import logging
import configparser
from datetime import datetime
#from os import getenv
config = configparser.ConfigParser()  # создаём объекта парсера
config.read("config.ini")  # читаем конфиг

bot = Bot(config["BOT"]["TOKEN_API"])
dp = Dispatcher(bot)

#logging.basicConfig(level=logging.INFO)
#Всякие переменные 
count = 0
number_of_inputs = 0
previous_message = ''# Переменная для хранения предыдущего сообщения
list_manufacors = ManufacorChoice()
#Конец всяких переменных

""" КЛАВИАТУРА """
kb = ReplyKeyboardMarkup(resize_keyboard=True) # parameter one_time_keyboard def=False
btn1 = KeyboardButton('Описание')
btn2 = KeyboardButton('Помощь')
kb.add(btn1).add(btn2) # insert(кнопка) - для нов столбика 

ikb = InlineKeyboardMarkup()
ibtn_names_tobacco = InlineKeyboardButton(text="Табаки", callback_data="names_tobacco")
ibtn_back = InlineKeyboardButton(text="Назад", callback_data="back_button") #Назад только один раз
ibtn_manufactor = InlineKeyboardButton(text="Производители", callback_data="manufacor")
ikb.add(ibtn_manufactor).add(ibtn_names_tobacco)

ikb_back_only = InlineKeyboardMarkup()
ill_come_back = InlineKeyboardButton(text= "Вернуться назад", callback_data="fuckgoback")
ikb_back_only.add(ill_come_back)
""" КОНЕЦ КЛАВИАТУРА """

async def on_startup(_):
    print("Стартуем!")

# Определение состояний FSM
class MenuStates(StatesGroup):
    main_menu = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    global previous_message
    await message.answer(text= START_TEXT, parse_mode="HTML", reply_markup = ikb) # написать
    previous_message = message.text

    if message.from_user.id == config["BOT"]["ADMIN_ID"]:
        keyboard_admin = types.ReplyKeyboardMarkup(row_width=2)
        buttons = [
            types.KeyboardButton(text="Список пользователей"),
            types.KeyboardButton(text="Отправить объявление"),
            types.KeyboardButton(text="Запрос3")
            # Добавь остальные кнопки
        ]
        keyboard_admin.add(*buttons)

        await message.answer("Меню команд", reply_markup=keyboard_admin)

        await MenuStates.main_menu.set()
    else:
        await message.answer("Вы не администратор бота.")
# Обработчик команды /cancel
@dp.message_handler(commands=["cancel"], state="*")
async def cancel(message: types.Message, state: FSMContext):
    # Проверяем, что идентификатор пользователя соответствует администратору бота
    if message.from_user.id == config["BOT"]["ADMIN_ID"]:
        await state.finish()

        keyboard_admin = types.ReplyKeyboardRemove()
        await message.answer("Вы отменили текущее действие.", reply_markup=keyboard_admin)
    else:
        await message.answer("Вы не администратор бота.")


# Обработчик сообщений для главного меню
@dp.message_handler(state=MenuStates.main_menu)
async def main_menu_handler(message: types.Message, state: FSMContext):
    # Проверяем, что идентификатор пользователя соответствует администратору бота
    if message.from_user.id == config["BOT"]["ADMIN_ID"]:
        if message.text == "Список пользователей":
            await message.answer("Вы выбрали: Список пользователей")
            await state.finish()
        elif message.text == "Отправить объявление":
            await message.answer("Вы выбрали: Отправить объявление")
            await state.finish()
        elif message.text == "Запрос3":
            await message.answer("Вы выбрали: Запрос3")
            await state.finish()    
        else:
            await message.answer("Выберите кнопку из меню.")
    else:
        await message.answer("Вы не администратор бота.")

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    global previous_message
    await message.answer(HELP_COMMAND) # ответить
    previous_message = message.text
    
@dp.message_handler(text = 'Помощь')
async def help_command(message: types.Message):
    global previous_message
    await message.answer(HELP_COMMAND, reply_markup=ikb_back_only) # ответить
    previous_message = message.text
    await message.delete()
        
@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    global previous_message 
    await message.answer(DESCRIPTION)
    previous_message = message.text
    
@dp.message_handler(text = 'Описание')
async def help_command(message: types.Message):
    await message.answer(DESCRIPTION, reply_markup=ikb_back_only) 
    await message.delete()     

@dp.message_handler(text = 'Пенис')
async def sticker_giver(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEJ9exk0oa87s2dqdLDTO0j6_g3tyYDbgAC1AsAAg74eUlJg1T3YVm93jAE")
   

@dp.message_handler(commands=['photo'])
async def send_penis(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://cdn-icons-png.flaticon.com/512/6147/6147668.png")
    

@dp.message_handler()
async def interception(message: types.Message): # проверка вводимых слов
    global number_of_inputs
    global previous_message
    while message.text != "Список пользователей":
        if message.text.count(' ') >= 1 and message.text:
            previous_message = message.text
            await message.answer(result(message.text), reply_markup=ikb_back_only)
        else:
            await message.answer(text = COUNT_ERROR, parse_mode="HTML", reply_markup=kb)
            number_of_inputs +=1
            if number_of_inputs > 2:
                await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEJ9exk0oa87s2dqdLDTO0j6_g3tyYDbgAC1AsAAg74eUlJg1T3YVm93jAE")
                number_of_inputs = 0
          

@dp.callback_query_handler(lambda callback_query: callback_query.data == 'names_tobacco') #Табаки
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text= find_all_names(), reply_markup=ikb_back_only)
    

@dp.callback_query_handler(text='back_button')
async def back_button_handler(query: types.CallbackQuery):
    global previous_message

    # Отправляем предыдущее сообщение
    if previous_message:
        await query.message.bot.send_message(query.from_user.id, previous_message)
        previous_message = ''

    # Удаляем кнопку
    await query.message.delete()    

@dp.callback_query_handler(lambda callback_query: callback_query.data == 'manufacor') #Производители и выбор одного из производителя
async def process_callback_button(callback_query: types.CallbackQuery):
    for i in range(len(list_manufacors)):# для удаления 'xlsx' из каждого объекта
        list_manufacors[i] = list_manufacors[i].replace('.xlsx', '')
    ikb_manufactors = InlineKeyboardMarkup()
    manufacturers_str = '\n'.join(list_manufacors)
    for var in list_manufacors:
        ikb_manufactors.add(InlineKeyboardButton(text= var, callback_data=var))
    ikb_manufactors.add(ill_come_back)    
    await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                text=f"Найдены производители:\n {manufacturers_str}\n⬇Выберите производителя табака⬇", reply_markup=ikb_manufactors) 
    @dp.callback_query_handler(lambda callback_query: True)
    async def process_callback(callback_query: types.CallbackQuery):
        # Получаем текст нажатой кнопки
        selected_variable = callback_query.data
        print(f"Пользователь выбрал: {selected_variable}")
        await bot.send_message(callback_query.from_user.id, f"Вы выбрали: {selected_variable}")
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
        await bot.send_message(callback_query.from_user.id, text= START_TEXT, parse_mode="HTML", reply_markup = ikb)
        str(selected_variable)
        v = selected_variable + ".xlsx"
        handle_variable(v)
        handle_variable2(v)

@dp.callback_query_handler(lambda callback_query: callback_query.data == 'fuckgoback')
async def back_back_button(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text= START_TEXT, parse_mode="HTML", reply_markup = ikb)      


#current_time = datetime.now()
#formatted_date = current_time.strftime("%Y-%m-%d %H:%M:%S")
#logging.basicConfig(
#        level=logging.DEBUG,
#        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
#        handlers=[
#            logging.FileHandler('bot.log'),
#            logging.StreamHandler(),
#        ],
#    )
#logging.debug('Старт программы')

if __name__ == "__main__":
    #logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
