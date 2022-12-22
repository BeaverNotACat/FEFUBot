from bot import bot
from bot.texts import hello
from bot.markups import hello_list

@bot.message_handler(commands=["start"])
def meeting_message(message):
    bot.send_message(message.from_user.id, hello, reply_markup=hello_list())
