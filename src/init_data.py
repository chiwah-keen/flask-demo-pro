#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2019年5月7日

@author: ljbai

@attention: 系统初始化数据脚本

@note: 
- 创建管理员
- 创建默认全局行业
'''

import hashlib
import datetime

from initialization.mongodb_process import mongo_cli


def create_admin():
    name = "超级管理员"
    account = "admin"
    role = "admin"
    document = {
        "name":name,
        "account":account,
        "pwd":encryption_pwd("ljbai"),
        "role":role,
        "is_live":1,
        "is_review":1,
        "ctime":current_now(),
        "uptime":current_now()
        }
    mongo_cli.single_insert("user", document)


def create_global_trade():
    name = "默认全局敏感词"
    code = "0000"
    words = [ 
        "他妈"
    ]
    document = {
        "name":name,
        "code":code,
        "words":words,
        "is_live":1,
        "ctime":current_now(),
        "uptime":current_now()
        }
    mongo_cli.single_insert("trade", document)

###################### 辅助函数 ####################
def encryption_pwd(pwd):
    """
    @attention: 密码加密
    """
    return hashlib.md5(pwd.encode("utf8")).hexdigest()


def current_now():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")


if __name__ == '__main__':
#     create_admin()
#     create_global_trade()
    print(encryption_pwd("ljbai"))
