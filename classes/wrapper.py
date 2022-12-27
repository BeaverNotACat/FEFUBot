import requests

# from classes.config import ALL_OBJECTS_URL, DEVICE_BY_ID_URL


class FefuMetaDB:
    """Representation of the FEFU MetaDB for Smast Campus """

    def __init__(self, device_by_id_url, all_objects_url):
        self.device_by_id_url = device_by_id_url
        self.all_objects_url = all_objects_url
        self.empty_dict = {
            "battery": 0, 
            "co2": 0, 
            "hum": 0, 
            "lux": 0, 
            "noise": 0, 
            "powertype": 0, 
            "temp": 0, 
            "tilt": 0, 
            "time": "---", 
            "type": 0
            }

    def __check_response(self, resp):
        return (resp == "<Response [200]>")

    def __empty_dict_with_err(self, text):
        repl = self.empty_dict.copy()
        repl["time"] = text
        return repl

    def request_objects_list(self) -> dict:
        return self.__validate_json(requests.get(self.all_objects_url).json())

    def __request_device_readings(self, device_id: int) -> dict:
        resp = requests.get(self.device_by_id_url+str(device_id))
        if self.__check_response(str(resp)):
            return self.__validate_json(resp.json())
        else:
            return self.__empty_dict_with_err(str(resp))


    def __get_devises_list(self, object_name):
        try:
            return self.request_objects_list()[object_name]['devices']
        except:
            return []


    @staticmethod
    def __validate_json(json: dict) -> dict:
        if not json:
            raise ValueError('json is empty')
        return json

    def get_devices_readings(self, object_name) -> dict:
        readings = {}
        for device in self.__get_devises_list(object_name):
            currnet_device_readings = self.__request_device_readings(device["device_id"])
            for readings_key in currnet_device_readings.keys():
                readings[readings_key] = currnet_device_readings[readings_key]
        return readings

    def get_objects_list(self):
        return self.request_objects_list().keys()