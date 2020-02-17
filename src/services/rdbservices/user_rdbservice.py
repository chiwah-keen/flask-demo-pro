#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2020年02月10日

@author: jianzhihua
'''
from utils.str_tools import json_loads, json_dumps
from initialization.redis_process import redis_cli
from conf.sysconf import REDIS_USER_SESSION_PREFIX


def get_user_session(userid):
    session_key = REDIS_USER_SESSION_PREFIX + str(userid)
    user_info = redis_cli.get(session_key)
    return json_loads(user_info)


def set_user_session(userid, user_info, expire=7 * 24 * 60 * 60):
    session_key = REDIS_USER_SESSION_PREFIX + str(userid)
    user_info = json_dumps(user_info)
    return redis_cli.setex(session_key, expire, user_info)




