#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2019年2月13日

@author: ljbai
'''
import traceback
import conf
import utils.redisdb as ur
from initialization.logger_processsor import logger
from utils.custom_mark import TipResponse

try:
    redis_cli = ur.create_default_redis(conf.REDIS_CONFIG)
#     redis_cli,_ = ur.create_sentinel_redis(confs.REDIS_CONFIG)
except:
    error_msg = traceback.format_exc()
    logger.warn(error_msg)
    raise TipResponse("redis初始化连接失败")


def lpop(key,number):
    pipeline = redis_cli.pipeline()
    for _ in range(number):
        pipeline.lpop(key)
    lines = pipeline.execute()
    return lines

setattr(redis_cli, "lpop", lpop)