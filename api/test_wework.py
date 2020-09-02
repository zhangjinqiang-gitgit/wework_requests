from work_request.api.wework import WeWork


class TestWeworkApi:
    def test_create(self):
        # userid, name, mobile
        print(WeWork().test_creat("004", "wang004", "17688898984"))