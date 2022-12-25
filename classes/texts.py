from classes.checking_funcs import Checking_funcs


class Texts:
    def __init__(self):
        self.check_obj = Checking_funcs()
        self.my_keys = ["time", "hum", "co2", "temp", "noise"]
        self.subscribing_text = '''Вы подписались'''
        self.hello_text = '''Давайте знакомиться, я - "мальчик, который кричал волки"'''
        self.choose_corp_text = '''Выберите корпус'''
        self.choose_cabinet_text = '''Вы выбрали корпус {}\nВыберите аудиторию'''
        self.cabinet_info_text = '''Информация по кабинету {name_cabinet}
        time - {time}
        влажность - {hum} % {hum_check}
        углекислый газ - {co2} ppm ({co2_1} %) {co2_check}
        температура - {temp} °С {temp_check}
        шум - {noise} дБ {noise_check}'''

    
    def hello(self):
        return self.hello_text

    def subscribing(self):
        return self.subscribing_text

    def buildings(self):
        return self.choose_corp_text

    def cabinets(self, corp):
        return self.choose_cabinet_text.format(corp)

    def cabinet_info(self, name_cabinet, dict_inf):
        my_dict = dict([(key, dict_inf.get(key)) for key in self.my_keys])
        my_dict["co2_1"] = round(my_dict.get("co2", 0) / 10000, 2)
        my_dict["name_cabinet"] = name_cabinet
        my_dict["hum_check"] = self.check_obj.hum(my_dict["hum"])
        my_dict["co2_check"] = self.check_obj.co2(my_dict["co2"])
        my_dict["temp_check"] = self.check_obj.temp(my_dict["temp"])
        my_dict["noise_check"] = self.check_obj.noise(my_dict["noise"])
        return self.cabinet_info_text.format(**my_dict)


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

