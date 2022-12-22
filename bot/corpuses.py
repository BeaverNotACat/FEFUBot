from bot import bot
from bot.texts import what_corp_you_want
from bot.markups import arr_of_corps

@bot.callback_query_handler(func=lambda call: (call.data == "list_corps") or (call.data == "from_hello"))
def list_of_corpuses(call):
    if call.data == "list_corps":
        bot.edit_message_text(what_corp_you_want, call.from_user.id, call.message.id, reply_markup=arr_of_corps())
    else:
        bot.send_message(call.from_user.id, what_corp_you_want, reply_markup=arr_of_corps())
    #bot.delete_message(call.from_user.id, call.message.id)



