#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2020年2月7日

@author: jianzhihua
'''
import json
from flask_app import main_app
from flask import request
from flask import session
from utils.custom_mark import NoAuthResponse


@main_app.before_request
def before_request():
    """
    @attention: 进入视图前执行的部分
    @note:
            一般做如下功能
    - 防攻击
    - 参数处理
    - 账号登录
    - 权限验证
    """
    data = {}
    print ("before requests....-----------")
    if request.method in ("POST", "PUT"):
        data = json.loads(request.data) if request.data else {}
    elif request.method in ("DELETE", "GET"):
        data = request.args

    setattr(request, 'bjson', data)

    no_auth_list = [
        ("/demo/company", "GET"),
    ]
    if (request.path, request.method) not in no_auth_list:
        is_authenticated()


@main_app.after_request
def after_request(response):
    """
    @attention: 执行视图后运行的部分
    @note:
    - 加密
    - 跨域
    - 国际化
    """
    response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin', "*")
    allow_headers = 'Content-Type, Authorization, token'
    response.headers.add('Access-Control-Allow-Headers', allow_headers)
    if 'Access-Control-Allow-Credentials' not in response.headers:
        response.headers.add('Access-Control-Allow-Credentials', "true")

    return response


def is_authenticated():
    user = session.get("user", {})
    print("------------")
    print(user)
    session['user_info'] = {'test': 123}
    if not user:
        raise NoAuthResponse()

