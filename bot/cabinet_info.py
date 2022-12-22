from bot import bot
from bot.markups import arr_of_inf
from bot import api

'''{
    'battery': 0, 
    'co2': 336, 
    'hum': 20, 
    'lux': 20, 
    'noise': 46, 
    'powertype': 2, 
    'temp': 23.5, 
    'tilt': 3, 
    'time': 'Wed, 21 Dec 2022 05:47:36 GMT', 
    'type': 1
}'''

info_to_user = '''Датчики аудитории
time - {time}
влажность - {hum} % (в пределах нормы)
углекислый газ - {co2} ppm ({co2_1} %) (в пределах нормы)
температура - {temp} °С (в пределах нормы)
шум - {noise} дБ (в пределах нормы)'''


my_keys = ["time", "hum", "co2", "temp", "noise"]

def making_message(dict_inf):
    my_dict = dict([(key, dict_inf.get(key)) for key in my_keys])
    my_dict["co2_1"] = round(my_dict.get("co2", 0) / 10000, 2)

    return info_to_user.format(**my_dict)

@bot.callback_query_handler(func=lambda call: call.data[:3] == "cab")
def get_info(call):
    cab = call.data[3:]
    new_text = "Вы выбрали кабинет " + cab + "\n"
    new_text += making_message(api.info_of_this_cabinet(cab))
    bot.edit_message_text(new_text, call.from_user.id, call.message.id, reply_markup=arr_of_inf(cab))
    # bot.delete_message(call.from_user.id, call.message.id)
    # bot.send_message(call.from_user.id, what_cabinet_you_want, reply_markup=arr_of_inf(cab))
    
