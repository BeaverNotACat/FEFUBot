import requests

from classes.config import ALL_OBJECTS_URL, DEVICE_BY_ID_URL


class FefuMetaDB:
  """Representation of the FEFU MetaDB for Smast Campus """

  def request_objects_list(self) -> dict:
    return self.__validate_json(requests.get(ALL_OBJECTS_URL).json())

  def __request_device_readings(self, device_id: int) -> dict:
    return self.__validate_json(requests.get(DEVICE_BY_ID_URL+str(device_id)).json())

  def __get_devises_list(self, object_name):
    return self.request_objects_list()[object_name]['devices']

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