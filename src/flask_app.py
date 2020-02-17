#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2019年12月17日

@author: ljbai
'''
import logging
from flask import Flask


main_app = Flask(__name__)
main_app.config['PROPAGATE_EXCEPTIONS'] = True       # 打开异常, 如果关闭， 500异常将不会被捕获
main_app.config['JSON_AS_ASCII'] = False        # 支持中文直接显示
logging.getLogger('werkzeug').disabled = False  # 关闭flask框架的日志记录，我们使用自定义的logger, True 关闭， False 打开

