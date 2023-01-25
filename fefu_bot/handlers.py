from fefu_bot import bot, lets_make_buttons, lets_make_texts, api


@bot.message_handler(commands=["start"])
def meeting_message(message):
    bot.send_message(message.from_user.id, lets_make_texts.hello(), reply_markup=lets_make_buttons.hello_button())

@bot.callback_query_handler(func=lambda call: call.data == "list_buildings")
def list_of_corpuses(call):
    bot.edit_message_text(lets_make_texts.buildings(), call.from_user.id, call.message.id, reply_markup=lets_make_buttons.list_buildings(api.all_buildings()))

@bot.callback_query_handler(func=lambda call: call.data[:4] == "corp")
def list_of_levels(call):
    bot.edit_message_text(lets_make_texts.levels(call.data[4:]), call.from_user.id, call.message.id, reply_markup=lets_make_buttons.list_levels(api.levels_of_this_building(call.data[4:])))

@bot.callback_query_handler(func=lambda call: call.data[:5] == "level")
def list_of_cabinets(call):
    bot.edit_message_text(lets_make_texts.cabinets(call.data[5:]), call.from_user.id, call.message.id, reply_markup=lets_make_buttons.list_cabinets(api.cabinets_of_this_level(call.data[5:])))

@bot.callback_query_handler(func=lambda call: call.data[:3] == "cab")
def get_info(call):
    bot.edit_message_text(lets_make_texts.cabinet_info(call.data[3:], api.cabinet_info(call.data[3:])), call.from_user.id, call.message.id, reply_markup=lets_make_buttons.back())

@bot.message_handler(content_types=["text"])
def list_of_corpuses(message):
    req = message.text
    if (len(message.text) <= 5) and ("A" <= req.upper() <= "Z") and (req[1:].isdecimal()):
        req = req[0].upper() + req[1:]
        bot.send_message(message.from_user.id, lets_make_texts.cabinet_info(req, api.cabinet_info(req)), reply_markup=lets_make_buttons.back())


