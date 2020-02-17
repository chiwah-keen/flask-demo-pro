#coding=utf-8
'''
Created on 2018年11月23日

@author: ljbai

@attention: 提供各种响应类异常封装,配合exception_processor使用
本文件在不是用RestFul 的情况下使用.
'''


class TipResponse(Exception):
    """
    @attention: 提示类响应
    """
    def __init__(self,msg):
        self.msg = msg
        
    def show(self):
        return self.msg


class ParamResponse(Exception):
    """
    @attention: 参数类响应
    @note: 
    data不能为空，为空时使用TipResponse
    """
    def __init__(self,msg,data):
        self.msg = msg
        assert data and isinstance(data, dict)
        self.data = data
        
    def show(self):
        return self.msg, self.data


class RedirectResponse(Exception):
    """
    @attention: 重定向响应
    """
    def __init__(self,curl):
        self.curl = curl
    
    def show(self):
        return self.curl


class NoAuthResponse(Exception):
    """
    @attention: 未授权
    """

    def __init__(self, msg="未登录"):
        self.msg = msg

    def show(self):
        return self.msg
