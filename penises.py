#wait bot.send_message(chat_id=message.from_user.id,
#                       text='Hello!') отправить в личку
#wait bot.send_message(chat_id=message.chat.id,
#                       text='Hello!') отправить в чат\группу
#dp.message_handler(commands=['photo'])
#async def send_adress(message: types.Message):
#   await bot.send_location(chat_id = message.from_user.id, latitude = 55, longitude = 74)
# message.capitalize()
@dp.message_handler()
async def interception(message: types.Message):
    if message.text.count(' ') >= 1:
        await message.answer(result(message.text))
    else:
        await message.answer(text = COUNT_ERROR, parse_mode="HTML")
        await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEJ9exk0oa87s2dqdLDTO0j6_g3tyYDbgAC1AsAAg74eUlJg1T3YVm93jAE")

