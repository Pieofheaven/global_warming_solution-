import telebot
import random
import logging
import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, Application, CommandHandler, ConversationHandler, CallbackQueryHandler


TOKEN = '9218772744:AAF06Eo6s7ICEUst6DyuizSLZmYX2G2GiK8'

bot = telebot.TeleBot(TOKEN)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


# Stages
START_ROUTES, END_ROUTES = range(2)
# Callback data
ONE, TWO, THREE, FOUR = range(4)


advice = {
    'Используйте общественный транспорт вместо частных автомобилей': ', таким образом уменьшаете в день ~2,5 кг,а в год ~900 кг CO2.',
    'Замените говядину на растительный белок или на птицу': ', таким образом уменьшаете в день ~3-5 кг (в день замены),а в год ~200-500 кг CO2.',
    'Снизите температуру в комнате на 1-2 °C': ', таким образом уменьшаете в день ~1,2 кг (в сезон),а в год ~250 кг CO2.',
    'Приниймайте душ на 3 минуты': ', таким образом уменьшаете в  день ~0,7 кг,а в год ~250 кг CO2.',
    'Сокращайте пищевые отходы': ', таким образом уменьшаете в день ~0,8 кг,а в год ~300 кг CO2.',
    'Делайте Стирку при 30 °C и выключите приборы из сети': ', таким образом уменьшаете в день ~0,6 кг,а в год ~220 кг CO2.'
}


async def startmsg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(ONE)),
            InlineKeyboardButton("2", callback_data=str(TWO)),
        ]
    ] 
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return START_ROUTES

@bot.message_handler(commands= ['clarify'])
def advice_clarifier(message):
    advices = message.text.split(maxsplit=1)[1]
    amount_saved = advice.get(advices)
    bot.send_message(message.chat.id, f"{advices}, {amount_saved}")

@bot.message_handler(commands= ['advice'])
def advice_list(message):
    advice_list = advice.keys()
    i = random.choice(list(advice_list))
    bot.send_message(message.chat.id, f'{i}')
    bot.send_message(message.chat.id, 'Напишите /clarify и предыдущее сообщение чтобы узнать побольше информации')

bot.infinity_polling()