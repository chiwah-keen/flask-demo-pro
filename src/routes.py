#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2019年12月17日

@author: ljbai
'''

from flask_api import main_api
from handler import demo, user_handler

# demo 示例
main_api.add_resource(demo.DemoHandler, '/demo')

# 登录
main_api.add_resource(user_handler.UserHandler, '/login')
