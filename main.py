import telebot
import random

TOKEN = '9218772744:AAGhpNQLjkaO_GIIWsGZBv8KExd_kIZDvC8'

bot = telebot.TeleBot(TOKEN)

advice = {
    'Используйте общественный транспорт вместо частных автомоболей': 'Таким образом уменьшаете в день ~2,5 кги в год ~900 кг СО2',
    'Замена говядины на растительный белок / птицу': 'Таким образом уменьшаете в день ~3-5 кг (в день замены), в год ~200–500 кг СО2',
    'Снижение температуры в комнате на 1–2 °C': 'Таким образом уменьшаете в день ~1,2 кг (в сезон), в год ~250 кг СО2',
    'Душ короче на 3 минуты': 'Таким образом уменьшаете в  день ~0,7 кг, в год ~250 кг СО2',
    'Сокращение пищевых отходов': 'Таким образом уменьшаете в день ~0,8 кг, в год ~300 кг СО2',
    'Стирка при 30 °C и выключение приборов из сети': 'Таким образом уменьшаете в день ~0,6 кг, в год ~220 кг СО2'
}

@bot.message_handler(commands= ['start'])
def startmsg(message):
    bot.send_message(message.chat.id, "Приветствую, этот бот поможет вам уменьшить количество СО2 вы помогаете выпускать в атмосферу. Напишите /advice чтобы начать")

@bot.message_handler(commands= ['help'])
def advice_clarifier(message):
    advices = message.text.split(maxsplit=1)[1]
    amount_saved = advice.get(advices)
    bot.send_message(message.chat.id, f"{advices}, {amount_saved}")

@bot.message_handler(commands= ['advice'])
def advice_list(message):
    advice_list = advice.keys()
    i = random.choice(list(advice_list))
    bot.send_message(message.chat.id, f'{i}')

bot.infinity_polling()