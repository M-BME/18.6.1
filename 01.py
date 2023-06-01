python
import telebot
from extensions import APIException, CurrencyConverter, CurrencyCodes

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start', 'help'])
def send_instructions(message):
    text = 'Привет! Я бот, который умеет конвертировать валюты. Чтобы узнать цену на определенное количество валюты, напишите сообщение в формате: \n<имя валюты цену которой вы хотите узнать> <имя валюты в которой надо узнать цену первой валюты> <количество первой валюты>\nНапример: "доллар рубль 100".\nЧтобы узнать список доступных валют, введите команду /values.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def send_currency_codes(message):
    currency_codes = CurrencyCodes.get_currency_codes()
    text = 'Доступные валюты:\n'
    for code in currency_codes:
        text += f'{code} - {currency_codes[code]}\n'
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def get_currency_price(message):
    try:
        base, quote, amount = message.text.split(' ')
        result = CurrencyConverter.get_price(base.upper(), quote.upper(), amount)
        text = f'{amount} {base.upper()} = {result} {quote.upper()}'
        bot.send_message(message.chat.id, text)
    except APIException as e:
        bot.send_message(message.chat.id, str(e))
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат сообщения. Введите сообщение в формате: \n<имя валюты цену которой вы хотите узнать> <имя валюты в которой надо узнать цену первой валюты> <количество первой валюты>\nНапример: "доллар рубль 100".')

bot.polling(none_stop=True)