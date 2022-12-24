import telebot
from classes.markups import Markups
from classes.texts import Texts
from classes.connect_with_api import APIInterface
from classes.subscribe import Mailing

with open("credential.txt") as F:
    bot_token = F.read().replace("\n", "")

bot = telebot.TeleBot(bot_token)

lets_make_buttons = Markups()
lets_make_texts = Texts()
api = APIInterface()
mailing = Mailing()
