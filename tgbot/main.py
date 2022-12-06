import telebot
from django.conf import settings
from . import keyboards as KB


bot = telebot.TeleBot(settings.BOT_TOKEN)

webhook_url = bot.get_webhook_info()

if webhook_url != settings.WEBHOOK_URL or webhook_url == '':
    bot.remove_webhook()
    bot.set_webhook(url=settings.WEBHOOK_URL)


@bot.message_handler(commands=['start'])
def start(msg):
	bot.send_message(msg.from_user.id, "Hello World!", reply_markup=KB.set_lang())
