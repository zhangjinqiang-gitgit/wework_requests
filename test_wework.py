import pytest
import requests

def test_create_data():
    " 创建企业微信成员构造数据 "
    # "userid,name,mobile"
    data  = [("lisi"+str(x),"李四","176%08d"%x) for x in range(20)]
    return data
class TestWework:
    """ 企业微信成员接口增删改查 """
    @pytest.fixture("module")
    def token(self):
        """ 获取企业微信token """
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        request_params = {
            "corpid": "ww4f3cdc369f8f3e3e",
            "corpsecret": "K7UZpgOxOoP148r_xSsfhqA7FX_Oh0DMCONprkodfV8"
        }
        r = requests.get(url, params=request_params)
        return r.json()['access_token']

    def test_creat(self,token,base_url,userid,name,mobile,department=None):
        """ 创建企业微信成员 """
        if department == None:
            department = [1]
        url = base_url + f"/create?access_token={token}"
        request_params = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = requests.post(url, json=request_params)
        # print(r.json())
        return r.json()

    def test_delete(self,token,base_url,userid):
        """ 删除企业微信成员 """
        url = base_url + f"/delete?access_token={token}"
        request_params = {
            "userid": userid
        }
        r = requests.get(url,params=request_params)
        # print(r.json())
        return r.json()

    def test_update(self,token,base_url,userid,name,mobile,department=None):
        """ 更新企业微信成员 """
        if department == None:
            department = [1]
        url = base_url + f"/update?access_token={token}"
        request_params = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = requests.post(url, json=request_params)
        # print(r.json())
        return r.json()

    def test_get(self,token,base_url,userid):
        """ 获取企业微信成员 """
        url = base_url + f"/get?access_token={token}"
        request_params = {
            "userid": userid
        }
        r = requests.get(url,params=request_params)
        # print(r.json())
        return r.json()

    @pytest.mark.parametrize("userid,name,mobile",test_create_data())
    def test_wework(self,token,userid,name,mobile):
        """ 整体流程测试 """
        # 并发执行命令 pytest test_wework.py -n auto
        # print(userid,name,mobile)
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/user"
        try:
            assert 'created' == self.test_creat(token, base_url, userid, name, mobile)['errmsg']
        except AssertionError as e:
            if "mobile existed" in e.__str__():
                ruserid = e.__str__().split(":")[1][:-1]
                self.test_delete(token, base_url, ruserid)
                assert 'created' == self.test_creat(token, base_url, userid, name, mobile)['errmsg']
        assert name == self.test_get(token,base_url,userid)['name']
        name = "李四666"
        assert "updated" == self.test_update(token,base_url,userid,name,mobile)["errmsg"]
        assert "李四666" == self.test_get(token, base_url, userid)['name']
        assert "deleted" == self.test_delete(token,base_url,userid)['errmsg']
        assert "userid not found" in self.test_delete(token,base_url,userid)['errmsg']