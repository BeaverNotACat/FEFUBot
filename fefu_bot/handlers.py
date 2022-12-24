from fefu_bot import bot, lets_make_buttons, lets_make_texts, api, mailing


@bot.message_handler(commands=["start"])
def meeting_message(message):
    if mailing.find_user(message.from_user.id):
        bot.send_message(message.from_user.id, lets_make_texts.hello(), reply_markup=lets_make_buttons.hello_button())
    else:
        bot.send_message(message.from_user.id, lets_make_texts.hello_with_mailing(), reply_markup=lets_make_buttons.hello_button_with_mailing())

@bot.callback_query_handler(func=lambda call: call.data == "list_buildings")
def list_of_corpuses(call):
    bot.edit_message_text(lets_make_texts.buildings(), call.from_user.id, call.message.id, reply_markup=lets_make_buttons.list_buildings(api.all_buildings()))

@bot.callback_query_handler(func=lambda call: call.data[:4] == "corp")
def list_of_cabinets(call):
    bot.edit_message_text(lets_make_texts.cabinets(call.data[4:]), call.from_user.id, call.message.id, reply_markup=lets_make_buttons.list_cabinets(api.cabinet_of_this_building(call.data[4:])))
    # bot.delete_message(call.from_user.id, call.message.id)
    # bot.send_message(call.from_user.id, what_cabinet_you_want, reply_markup=arr_of_cabinets(corp))

@bot.callback_query_handler(func=lambda call: call.data[:3] == "cab")
def get_info(call):
    bot.edit_message_text(lets_make_texts.cabinet_info(call.data[3:], api.cabinet_info(call.data[3:])), call.from_user.id, call.message.id, reply_markup=lets_make_buttons.back())

@bot.callback_query_handler(func=lambda call: call.data == "subscription")
def subscription(call):
    bot.send_message(call.from_user.id, lets_make_texts.subscribing(), reply_markup=lets_make_buttons.hello_button())