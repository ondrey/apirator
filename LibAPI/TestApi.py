# -*- coding: utf-8 -*-


import ObjectAPI


class TestApi(ObjectAPI.ObjectAPI):
    def __init__(self):
        ObjectAPI.ObjectAPI.__init__(self)

    def api_asd(self):
        return '123'