#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2020年02月07日

@author: jianzhihua
'''

from flask_jwt_extended import JWTManager
from flask_api import main_app
from conf.base import SECRET_KEY

main_app.config['JWT_SECRET_KEY'] = SECRET_KEY
main_jwt = JWTManager(main_app)