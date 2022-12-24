from telebot import types

class Markups:
    def __make_buttons(self, ordered_buttons):
        list_of_buttons = types.InlineKeyboardMarkup()
        for text, call in ordered_buttons:
            msg = types.InlineKeyboardButton(text=text, callback_data=call)
            list_of_buttons.add(msg)
        return list_of_buttons

    def __make_correct_list(self, need_list, word):
        return self.__make_buttons([(name, word+str(name)) for name in need_list])


    def hello_button_with_mailing(self):
        return self.__make_buttons([("узнать состояние кампуса", "list_buildings"), ("подписаться", "subscription")])

    def hello_button(self):
        return self.__make_buttons([("узнать состояние кампуса", "list_buildings")])

    def list_buildings(self, list_of_buildings):
        return self.__make_correct_list(list_of_buildings, "corp")

    def list_cabinets(self, list_of_cabinets):
        return self.__make_correct_list(list_of_cabinets, "cab")
    
    def back(self):
        return self.__make_buttons([("назад", "list_buildings")])

#  + [("назад", "list_buildings")]
