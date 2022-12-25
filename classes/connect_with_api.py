from classes.wrapper import FefuMetaDB

connect_with_fefu = FefuMetaDB()

class APIInterface:

    def all_buildings(self):
        names = list(connect_with_fefu.get_objects_list())
        res = list()
        for name in names:
            if name[:6] == "Корпус":
                res.append(name)
        return sorted(res, key=lambda x: x[-1])

    def cabinet_of_this_building(self, corp):
        names = list(connect_with_fefu.request_objects_list()[corp]["children_all_levels"])
        return sorted([a for a in names if (a[0] == corp[-1])], key=lambda x: int(x[1:]))
    
    def cabinet_info(self, cab):
        return connect_with_fefu.get_devices_readings(cab)

