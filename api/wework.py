import yaml
import json
from work_request.api.baseapi import BaseApi
from work_request.api.util import Util


class WeWork(BaseApi):

    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = self.token
        with open("./wework.yaml",encoding="utf-8") as f:
            self.data = yaml.load(f)
            print(json.dumps(self.data['create'],indent=2))

    def test_creat(self, userid, name, mobile, department=None):
        """ 创建企业微信成员 """
        if department == None:
            department = 1
        self.params["userid"] = userid
        self.params["mobile"] = mobile
        self.params["name"] = name
        self.params["department"] = department
        return self.send(self.data["create"])

    
