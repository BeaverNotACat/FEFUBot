from bot import bot
from bot.texts import what_cabinet_you_want
from bot.markups import arr_of_cabinets

@bot.callback_query_handler(func=lambda call: call.data[:4] == "corp")
def list_of_cabinets(call):
    corp = call.data[4:]
    new_text = "Вы выбрали корпус " + corp + "\n"
    new_text += what_cabinet_you_want
    bot.edit_message_text(new_text, call.from_user.id, call.message.id, reply_markup=arr_of_cabinets(corp))
    # bot.delete_message(call.from_user.id, call.message.id)
    # bot.send_message(call.from_user.id, what_cabinet_you_want, reply_markup=arr_of_cabinets(corp))
    
