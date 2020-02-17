#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019年1月14日
@author: ljbai
"""
import os
import logging

import conf

# 日志配置
if not os.path.exists(conf.LOG_DIR):
    os.makedirs(conf.LOG_DIR)

logger = logging.getLogger(conf.PROJECT_NAME)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s||%(levelname)s||%(pathname)s||%(funcName)s||%(lineno)s||%(message)s')


class LogLevelFilter(logging.Filter):

    def __init__(self, name='', level=logging.DEBUG):
        super(LogLevelFilter, self).__init__(name)
        self.level = level

    def filter(self, record):
        return record.levelno == self.level


# 调试日志，定位BUG的时候使用
debug_handler = logging.FileHandler(os.path.join(conf.LOG_DIR, "operate.log"))
debug_handler.setLevel(logging.DEBUG)
debug_handler.addFilter(LogLevelFilter(level=logging.DEBUG))
debug_handler.setFormatter(formatter)

# 常规日志，常规记录
info_handler = logging.FileHandler(os.path.join(conf.LOG_DIR, "code.log"))
info_handler.setLevel(logging.INFO)
info_handler.addFilter(LogLevelFilter(level=logging.INFO))
info_handler.setFormatter(formatter)

# 警告日志,大部分该日志需要定位处理
warn_handler = logging.FileHandler(os.path.join(conf.LOG_DIR, "warn.log"))
warn_handler.setLevel(logging.WARN)
warn_handler.addFilter(LogLevelFilter(level=logging.WARN))
warn_handler.setFormatter(formatter)

# 异常日志
error_handler = logging.FileHandler(os.path.join(conf.LOG_DIR, "error.log"))
error_handler.setLevel(logging.ERROR)
error_handler.addFilter(LogLevelFilter(level=logging.ERROR))
error_handler.setFormatter(formatter)

logger.addHandler(debug_handler)
logger.addHandler(info_handler)
logger.addHandler(warn_handler)
logger.addHandler(error_handler)


def save_operate(msg):
    logger.debug(msg)


def save_log(msg):
    print(msg)
    logger.info(msg)


def save_time_sctrip(msg):
    print(msg)
    logger.warn(msg)
