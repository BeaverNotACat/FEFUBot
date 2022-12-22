from telebot import types
from bot import api

def hello_list():
    list_of_buttons = types.InlineKeyboardMarkup()
    msg = types.InlineKeyboardButton(text="узнать состояние кампуса", callback_data="from_hello")
    list_of_buttons.add(msg)
    return list_of_buttons

def make_buttons(word, args):
    list_of_buttons = types.InlineKeyboardMarkup()
    for i in args:
        msg = types.InlineKeyboardButton(text=i, callback_data=word + str(i))
        list_of_buttons.add(msg)
    if word != "corp":
        msg = types.InlineKeyboardButton(text="назад", callback_data="list_corps")
        list_of_buttons.add(msg)
    return list_of_buttons


def arr_of_corps():
    return make_buttons("corp", api.all_corpuses())

def arr_of_cabinets(corp):
    return make_buttons("cab", api.cabinet_of_this_corp(corp))

def arr_of_inf(cab):
    return make_buttons("", [])


