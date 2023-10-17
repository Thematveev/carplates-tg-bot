from telebot import TeleBot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import parser
from parser.helpers import check_info_fullness, combine_dicts


import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

TOKEN = "6498698131:AAHEETA69Y5uS1BQi39vJCLttgZFFrLpsUc"
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(msg: Message):
    print(msg)
    bot.send_message(msg.chat.id, "Привіт, відправ мені номерний знак авто у такому форматі - АА0000АА")


@bot.message_handler(regexp=r'[0-9a-zA-Zа-яіА-ЯІ]{2}\d{4}[0-9a-zA-Zа-яіА-ЯІ]{2}')
def search_info(msg: Message):
    p = msg.text.upper()
    result = parser.get_plates_info(p)
    if not check_info_fullness(result):
        additional_data = parser.get_plates_info_mtsbu(p)
        result = combine_dicts(result, additional_data)

    url_to_images = f'https://www.google.com/search?tbm=isch&q=%22{result["vin"]}%22'

    bot.send_message(
        msg.chat.id,
        f"Привіт, ось результати пошуку авто за номерним знаком {p}\n"
        f"Марка та модель -> {result['model']}\n"
        f"VIN-номер -> {result['vin']}\n"
        f"Рік випуску -> {result['year']}\n"
        f"Додаткові характеристики -> {result['specs']}\n",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Фото авто в Google Images', url=url_to_images)]
        ])
    )

bot.polling()