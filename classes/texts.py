
class Texts:
    def __init__(self):
        self.hello_text_with_mailing = '''Давайте знакомиться, я - "мальчик, который кричал волки"\n Вы можете подписаться на наши уведомления'''
        self.hello_text = '''Давайте знакомиться, я - "мальчик, который кричал волки"'''
        self.choose_corp_text = '''Выберите корпус'''
        self.choose_cabinet_text = '''Вы выбрали корпус {}\nВыберите аудиторию'''
        self.cabinet_info_text = '''Информация по кабинету {} noise - {noise}'''
        self.subscribing_text = '''Вы подписались'''

    def hello_with_mailing(self):
        return self.hello_text_with_mailing
    
    def hello(self):
        return self.hello_text

    def subscribing(self):
        return self.subscribing_text

    def buildings(self):
        return self.choose_corp_text

    def cabinets(self, corp):
        return self.choose_cabinet_text.format(corp)

    def cabinet_info(self, name_cabinet, dict_inf):
        return str(dict_inf)
        # return self.cabinet_info_text.format(name_cabinet, dict_inf)


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

# info_to_user = '''Датчики аудитории
# time - {time}
# влажность - {hum} % (в пределах нормы)
# углекислый газ - {co2} ppm ({co2_1} %) (в пределах нормы)
# температура - {temp} °С (в пределах нормы)
# шум - {noise} дБ (в пределах нормы)'''


# my_keys = ["time", "hum", "co2", "temp", "noise"]

# def making_message(dict_inf):
#     my_dict = dict([(key, dict_inf.get(key)) for key in my_keys])
#     my_dict["co2_1"] = round(my_dict.get("co2", 0) / 10000, 2)

#     return info_to_user.format(**my_dict)

