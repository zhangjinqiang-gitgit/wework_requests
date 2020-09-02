
import requests
import json
class BaseApi:

    params = {}

    def send(self,data):
        print("data_type",type(data))
        raw_data = json.dumps(data)
        print("raw_data_type",type(raw_data))
        for key, value in self.params.items():
            print("*******************",key,value)
            raw_data = raw_data.replace("${" + str(key) + "}", str(value))
        data = json.loads(raw_data)
        print("data=============", data)
        # print("=============",requests.request(**data).json())
        return requests.request(**data).json()