#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2017年9月13日

@author: jianzhihua

@note: 配置直接在最下面！
"""


def create_sentinel_redis(config):
    host_port = parse_host(config["host-port"])
    sentinel = Sentinel(host_port, socket_timeout=2, password=config['pwd'], db=config['db'])
    master = sentinel.master_for('mymaster', socket_timeout=5)
    slave = sentinel.slave_for('mymaster', socket_timeout=2)
    return master, slave


def create_default_redis(config):
    """
    @attention: 创建一个默认的redis环境
    """
    host_port = parse_host(config["host-port"])[0]
    connect = redis.StrictRedis(
        host=host_port[0], port=host_port[1], db=config["db"], password=config["pwd"])
    return connect


def parse_host(val):
    """
    @attention: 分解host,把10.1.113.158-26379分割为("10.1.113.158",26379)
    """
    info = re.findall(r"([\d\.]+)-(\d+)", val)
    return [(item[0], int(item[1])) for item in info]


if __name__ == '__main__':
    a = "10.1.113.158-26379"
    print(parse_host(a))
