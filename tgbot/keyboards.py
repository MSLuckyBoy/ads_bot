from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def set_lang(_):
	markup = InlineKeyboardMarkup()
	markup.add(
		InlineKeyboardButton(text=_("ru_keyboard"), callback_data="ru"),
		InlineKeyboardButton(text=_("uz_keyboard"), callback_data="uz")
	)
	return markup


def set_region(_):
	markup = InlineKeyboardMarkup(row_width=2)
	markup.add(
		InlineKeyboardButton(text=_("tashkent_keyboard"), callback_data="tashkent"),
		InlineKeyboardButton(text=_("samarkand_keyboard"), callback_data="samarkand"),
		InlineKeyboardButton(text=_("bukhara_keyboard"), callback_data="bukhara"),
		InlineKeyboardButton(text=_("andijan_keyboard"), callback_data="andijan"),
		InlineKeyboardButton(text=_("jizzakh_keyboard"), callback_data="jizzakh"),
		InlineKeyboardButton(text=_("qashqadaryo_keyboard"), callback_data="qashqadaryo"),
		InlineKeyboardButton(text=_("navoiy_keyboard"), callback_data="navoiy"),
		InlineKeyboardButton(text=_("namangan_keyboard"), callback_data="namangan"),
		InlineKeyboardButton(text=_("surxondaryo_keyboard"), callback_data="surxondaryo"),
		InlineKeyboardButton(text=_("sirdaryo_keyboard"), callback_data="sirdaryo"),
		InlineKeyboardButton(text=_("fergana_keyboard"), callback_data="fergana"),
		InlineKeyboardButton(text=_("xorazm_keyboard"), callback_data="xorazm"),
		InlineKeyboardButton(text=_("karakalpakstan_keyboard"), callback_data="karakalpakstan"),		
	)
	return markup


def menu(_):
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add(
		KeyboardButton(_("add_new_ad_keyboard"))
	)
	markup.add(
		KeyboardButton(_("see_ads_keyboard")),
		KeyboardButton(_("personal_cabinet_keyboard"))
	)
	return markup







