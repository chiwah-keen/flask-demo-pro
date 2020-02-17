#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2019年12月17日

@author: ljbai
'''

from flask_app import main_app
from flask_restful import Api

from flask_cors import CORS

CORS(main_app)
main_api = Api(main_app)


