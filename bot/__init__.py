import telebot
from secret_inf import bot_token
from classes.api_interface import APIInterface


bot = telebot.TeleBot(bot_token)
api = APIInterface()

