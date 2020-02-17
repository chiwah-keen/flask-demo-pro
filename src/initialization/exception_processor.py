#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2018年11月27日

@author: ljbai
"""
import traceback

# 三方库
from flask import request

from flask_app import main_app
from initialization.logger_processsor import logger

import utils.custom_mark as ucm
import utils.custom_response as ucr


@main_app.errorhandler(ucm.RedirectResponse)
def RedirectHandle(error): 
    """
    @attention: 重定向
    """
    curl = error.show()
    return ucr.op_redirect(curl)


@main_app.errorhandler(ucm.TipResponse)
def TipHandle(error):
    """
    @attention: 提示
    """
    msg = error.show()
    return ucr.op_fail(msg)


@main_app.errorhandler(ucm.NoAuthResponse)
def NoAuthHandle(error):
    """
    @attention: 提示
    """
    msg = error.show()
    return ucr.op_fail(msg, status=401)


@main_app.errorhandler(ucm.ParamResponse)
def ParamHandle(error):
    """
    @attention: 带参数提示
    """
    msg,  data = error.show()
    return ucr.op_fail(msg, data)


@main_app.errorhandler(Exception)
def BaseHandle(error):
    """
    @attention: 未知异常
    """
    traceback.print_exc()
    error_msg = traceback.format_exc()
    url_data = "url(%s):%s" % (request.url, request.method)
    get_data = "get_data:%s" % dict(request.args)
    json_data = "json_data:%s" % request.bjson
    error_data = "error_msg:%s" % error_msg
    log_msg = "\n".join([url_data, get_data, json_data, error_data])
    logger.warn(log_msg)
    msg = "System error"
    return ucr.op_fail(msg)

