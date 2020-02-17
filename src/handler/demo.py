#coding=utf-8
'''
Created on 2020-02-07

@author: jianzhihua

@attention:
'''
from .base_handler import BaseHandler
from services.jwt_operator import is_login


class DemoHandler(BaseHandler):

    @is_login
    def get(self):
        a = self.params
        print ("-----------------", a)
        return {'test': a}
