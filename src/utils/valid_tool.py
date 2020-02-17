#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2019年2月12日

@author: ljbai

@attention: 提供一些验证函数，可持续扩展
'''
import re

import utils.custom_mark as cm

tip = cm.TipResponse


def valid_none(val,label):
    if val is None:
        raise tip("%s不能为空" % label)


def valid_none_or_empty(val, label):
    if val is None or not val:
        raise tip("%s不能为空" % label)


def valid_email(email):
    """
    @attention: 检查邮箱复杂程度
    """
    info = re.findall(r"^\w+([-_.]+\w+)*@(\w+[-.])+\w{2,4}$", email, re.IGNORECASE)
    if not info:
        raise tip("邮箱格式不正确")


def valid_phone(phone):
    """
    @attention: 检查手机号码复杂程度
    """
    if len(phone) != 11 or (not phone.startswith("1")):
        raise tip(u"手机号码格式不正确")


def valid_gold(gold,label,is_float=False):
    """
    @attention: 检测金额必须是数字,且为正数
    """
    if isinstance(gold, str):
        try:
            if is_float:
                gold = float(gold)
            else:
                gold = int(gold)
        except:
            raise tip("%s必须为数字"%label)
    elif isinstance(gold, int):
        pass
    elif isinstance(gold, float):
        if not is_float:
            raise tip("%s必须为整数"%label)
    else:
        raise tip("%s必须为数字"%label)
    
    if gold<0:
        raise tip("%s必须大于0"%label)
    
    return gold

