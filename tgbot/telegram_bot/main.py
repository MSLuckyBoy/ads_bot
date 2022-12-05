import telebot
from django.conf import settings

from . import keyboards as KB

bot = telebot.TeleBot(settings.BOT_TOKEN)

bot.remove_webhook()
bot.set_webhook(url=f"https://{settings.WEBHOOK_URL_HOST}/{settings.WEBHOOK_URL_PATH}")


@bot.message_handler(commands=['start'])
def start(msg):
	bot.send_message(msg.from_user.id, "Hello World!")
