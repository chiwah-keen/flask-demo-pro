#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2020年02月07日

@author:  jianzhihua
"""

from flask_app import main_app
from initialization.logger_processsor import logger

import utils.custom_response as ucr


@main_app.errorhandler(404)
def S404Handle(error):
    """
    @attention: 404服务器警告异常
    """
    # msg,data = error.show()
    return ucr.op_fail(msg='Resource Not Found Error!', data={}, status=404)


@main_app.errorhandler(405)
def S405Handle(error):
    """
    @attention: 405服务器警告异常
    """
    # msg,data = error.show()
    return ucr.op_fail(msg='The method is not allowed for the requested URL!', data={}, status=405)


@main_app.errorhandler(500)
def S500Handle(error):
    """
    @attention: 500服务器警告异常
    """
    # msg,data = error.show()
    # return ucr.op_fail(msg='System Error!', data={}, status=500)
    return ucr.op_fail(msg='System Error!', data={}, status=500)

