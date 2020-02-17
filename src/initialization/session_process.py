#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2019年2月14日

@author: ljbai
'''
from flask_session import Session

from flask_app import main_app
import conf
from initialization.redis_process import redis_cli

main_app.secret_key = conf.SECRET_KEY
main_app.permanent_session_lifetime = conf.SESSION_TIMEOUT  # 设置session超时时间

main_app.config['SESSION_TYPE'] = 'redis'  # session类型为redis
main_app.config['SESSION_PERMANENT'] = False  # 如果设置为True，则关闭浏览器session就失效。
main_app.config['SESSION_USE_SIGNER'] = True  # 是否对发送到浏览器上session的cookie值进行加密
# 保存到session中的值的前缀
main_app.config['SESSION_KEY_PREFIX'] = conf.SESSION_KEY_PREFIX
main_app.config['SESSION_REDIS'] = redis_cli

Session(main_app)
