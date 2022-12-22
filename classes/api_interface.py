from classes.wrapper import FefuMetaDB
from random import random

connect_with_fefu = FefuMetaDB()

class APIInterface:
    def __init__(self):
        pass

    def all_corpuses(self):
        names = list(connect_with_fefu.get_objects_list())
        res = list()
        for name in names:
            if name[:6] == "Корпус":
                res.append(name)
        return res

    def cabinet_of_this_corp(self, corp):
        names = list(connect_with_fefu.request_objects_list()[corp]["children_all_levels"])
        res = [a for a in names if (a[0] == corp[-1])]
        # for name in names:
            # if (name[0] == corp[-1]):
                # res.append(name)
        return res
    
    def info_of_this_cabinet(self, cab):
        return connect_with_fefu.get_devices_readings(cab)



        



