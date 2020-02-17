#coding=utf-8
"""
@attention: 配置部分

@note: 
- 一份基础配置,定义不随环境变化的业务变量
- 每个人都创建自己的配置,不要配置127.0.0.1的方式,尽量使用IP
- 需要使用谁的环境,直接引用即可

"""

from conf.base import *
from conf.sysconf import *
# from confs.kailyn_local_config import *
# from confs.zk_config import *
