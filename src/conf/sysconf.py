#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019年1月14日

@author: ljbai
"""
import os
from .loader import conf_loader


CURR_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(os.path.dirname(CURR_PATH))

# 日志文件夹
# LOG_DIR = os.path.join(PROJECT_PATH, "logs", PROJECT_NAME)
LOG_DIR = os.path.join(PROJECT_PATH, "logs", "")

REDIS_USER_SESSION_PREFIX = "us_"                # user session prefix in redis.

REDIS_USER_SESSION_TIMEOUT = 7 * 24 * 60 * 60    # user session timeout.

REDIS_CONFIG = {
    "host-port": conf_loader('REDIS_HOST_PORT', '127.0.0.1:6379'),
    "pwd": "",
    "db": "7",
}


