class Checking_funcs:
    def __init__(self):
        self.good_result = "(в пределах нормы)"
        self.up_result = "(слишком высокое значение)"
        self.low_result = "(слишком низкое значение)"
        self.no_result = "(---)"


    def hum(self, num):
        if num:
            if num <= 14:
                return self.low_result
            return self.good_result
        return self.no_result
    
    def co2(self, num):
        if num:
            if num >= 3000:
                return self.up_result
            return self.good_result
        return self.no_result
    
    def temp(self, num):
        if num:
            if num >= 26:
                return self.up_result
            if num <= 15:
                return self.low_result
            return self.good_result
        return self.no_result
    
    def noise(self, num):
        if num:
            if num >= 80:
                return self.up_result
            return self.good_result
        return self.no_result