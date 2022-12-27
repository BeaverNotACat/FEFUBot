from classes.wrapper import FefuMetaDB


class APIInterface:
    def __init__(self, device_by_id_url, all_objects_url):
        self.connect_with_fefu = FefuMetaDB(device_by_id_url, all_objects_url)

    def all_buildings(self):
        names = list(self.connect_with_fefu.get_objects_list())
        res = list()
        for name in names:
            if (name[:6] == "Корпус") and ("A" <= name[-1] <= "Z"):
                res.append(name)
        return sorted(res, key=lambda x: x[-1])

    def levels_of_this_building(self, corp):
        names = list( self.connect_with_fefu.request_objects_list()[corp]["children_all_levels"])
        return sorted(set(a[:2] for a in names if (a[0] == corp[-1])), key=lambda x: int(x[1:]))

    def cabinets_of_this_level(self, level):
        names = list( self.connect_with_fefu.request_objects_list()["Корпус " + level[0]]["children_all_levels"])
        return sorted([a for a in names if (a[:2] == level)], key=lambda x: int(x[1:]))
    
    def cabinet_info(self, cab):
        return  self.connect_with_fefu.get_devices_readings(cab)

