import requests


class Util:
    def get_token(self):
        """ 获取企业微信token """
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        request_params = {
            "corpid": "ww4f3cdc369f8f3e3e",
            "corpsecret": "K7UZpgOxOoP148r_xSsfhqA7FX_Oh0DMCONprkodfV8"
        }
        r = requests.get(url, params=request_params)
        return r.json()['access_token']