import telebot
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateRedisStorage

from django.conf import settings

from tgbot.models import User

from tgbot import keyboards
from tgbot.redis_cache import RedisCache
from tgbot.middlewares import I18N


#Redis
cache = RedisCache()
state_storage = StateRedisStorage()


bot = telebot.TeleBot(settings.BOT_TOKEN, state_storage=state_storage, use_class_middlewares=True)


webhook_url = bot.get_webhook_info()

#Set webhook
if webhook_url != settings.WEBHOOK_URL or webhook_url == '':
    bot.remove_webhook()
    bot.set_webhook(url=settings.WEBHOOK_URL)


#Localization middleware
class I18NMiddleware(I18N):
	def process_update_types(self) -> list:
		return ['message', 'callback_query']
	
	def get_user_language(self, obj):
		user_id = obj.from_user.id

		if cache.get(user_id) is None: 
			cache.set(user_id, language="ru")
		
		return cache.get(user_id)["language"]


#Localization
i18n = I18NMiddleware(translations_path="locales", domain_name="messages")
_ = i18n.gettext


#States
class RegisrationState(StatesGroup):
	language = State()
	region = State()


# /start command
#-------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def start(msg):
	bot.set_state(msg.from_user.id, RegisrationState.language, msg.chat.id)
	bot.send_message(msg.from_user.id, _("choose_language_text"), reply_markup=keyboards.set_lang(_))

#-------------------------------------------------------------------


# User registration
#-------------------------------------------------------------------
@bot.callback_query_handler(func=lambda call:True, state=RegisrationState.language)
def set_language(call):
	bot.edit_message_text(_("choose_region_text"), call.from_user.id, call.message.id, reply_markup=keyboards.set_region(_))
	bot.set_state(call.from_user.id, RegisrationState.region, call.message.chat.id)

	with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
		data["language"] = call.data


@bot.callback_query_handler(func=lambda call:True, state=RegisrationState.region)
def set_region(call):
	bot.delete_message(call.from_user.id, call.message.id)
	bot.send_message(call.from_user.id, _("successful_registration_text"), reply_markup=keyboards.menu(_))

	with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
		user = User.objects.create(
			chat_id=call.from_user.id,
			first_name=call.from_user.first_name,
			username=call.from_user.username,
			language=data['language'],
			region = call.data 
		)
		cache.set(key=user.chat_id, language=user.language, region=user.region)

	bot.delete_state(call.from_user.id, call.message.chat.id)

#-------------------------------------------------------------------

bot.setup_middleware(i18n)
bot.add_custom_filter(custom_filters.StateFilter(bot))
