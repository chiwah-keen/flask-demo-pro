#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2020年02月06日

@author: jianzhihua

配置加载器
"""
import os

conf_dict = {}


def load_from_file(file_path=None):
    '''
    @param file_path
    从配置文件中加载配置
    '''
    file_path = file_path or env_loader('CONF_FILE_PATH') or "/run/secrets/global.conf"
    if os.path.exists(file_path):
        with open(file_path) as infile:
            for line in infile:
                if not line.strip() or line.strip().startswith("#") or '=' not in line:
                    continue
                tlist = line.strip().split('=')
                if len(tlist) != 2:
                    continue
                key, val = tlist
                conf_dict[key] = val
    return conf_dict


def file_loader(key):
    if not conf_dict: load_from_file()
    return conf_dict[key] if key in conf_dict else None


def env_loader(key):
    '''
    从环境变量中加载
    '''
    return os.environ[key] if key in os.environ else None


def conf_loader(key, default):
    '''
    配置加载器， 优先从环境变量中加载， 如果没有从配置文件中加载
    '''
    return env_loader(key) or file_loader(key) or default
