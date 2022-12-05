from telebot import types


def set_lang():
	markup = types.InlineKeyboardMarkup()
	markup.add(
		types.InlineKeyboardButton(text="RUS", callback_data="ru"),
		types.InlineKeyboardButton(text="UZB", callback_data="uz")
	)
	return markup


def set_region():
	markup = types.InlineKeyboardMarkup()
	markup.add(
		types.InlineKeyboardButton(text="TASHKENT", callback_data="tashkent"),
		types.InlineKeyboardButton(text="ANDIJAN", callback_data="andijan"),
		types.InlineKeyboardButton(text="SAMARKAND", callback_data="samarkand")
	)
	return markup


def menu():
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add(
		types.KeyboardButton("🆕 Добавить объявление")
	)
	markup.add(
		types.KeyboardButton("🔍 Посмотреть объявления"),
		types.KeyboardButton("🏡 Личный кабинет")
	)
	return markup







