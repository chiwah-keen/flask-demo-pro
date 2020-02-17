#!/usr/bin/env python
# coding:utf-8

import json, traceback
from initialization.logger_processsor import logger


def json_loads(json_str):
    try:
        return json.loads(json_str)
    except Exception  as e:
        logger.error(traceback.format_exc())
        return None


def json_dumps(json_obj):
    try:
        return json.dumps(json_obj)
    except Exception as e:
        logger.error(traceback.format_exc())
        return None
