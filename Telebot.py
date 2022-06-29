import telebot
from config import TOKEN, keys
from utils import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Привет! Я ТелеБот-Конвертер валют и вот, что я могу:  \n- Показать список доступных валют. Для этого вам достаточно запустить команду /values \
    \n- Я могу вывести конвертацию валюты через команды <имя валюты> <в какую валюту перевести> <количество переводимой валюты>\n \
- Если не запомнили, то я могу напомнить через команду /help'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Неправильные параметры')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Не удалось обработать команду. Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду. \n{e}')
    else:
        text = f'Цена {amount} {quote} = {base} - {total_base}'
        bot.send_message(message.chat.id, text)



bot.polling(none_stop=True)