import telebot
import yaml
from yaml.loader import SafeLoader

from classes.markups import Markups
from classes.texts import Texts
from classes.connect_with_api import APIInterface
from classes.subscribe import Mailing


with open("settings.yml", 'r') as stream:
    settings = yaml.load(stream, SafeLoader)
    bot_token = settings['token']
    device_by_id_url = settings['device_by_id_url']
    all_objects_url = settings['all_objects_url']


bot = telebot.TeleBot(bot_token)

lets_make_buttons = Markups()
lets_make_texts = Texts()
api = APIInterface(device_by_id_url, all_objects_url)
mailing = Mailing()
