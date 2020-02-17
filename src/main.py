#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2019年12月17日

@author: ljbai
'''

from flask_app import main_app

# 初始化,引用就来就算初始化了
from initialization import exception_processor
from initialization import httpexception_processor
from initialization import redis_process
from initialization import logger_processsor
# from initialization import session_process     # jwt 和 session 是两种认证方式不要同时选择
from initialization import jwtextend_process     # jwt 和 session  是两种认证方式不要同时选择
from initialization import sqlalchemy_process

import services.jwt_operator
#  初始化路由
import routes


if __name__ == "__main__":
    main_app.run(host="0.0.0.0", port=5001, debug=True)
