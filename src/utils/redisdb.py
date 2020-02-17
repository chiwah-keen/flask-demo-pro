#coding=utf-8
'''
Created on 2018年11月23日

@author: ljbai

@attention: 提供redis哨兵模式(分布式)接口,单机模式接口
'''
import re
from initialization.logger_processsor import logger
from redis.sentinel import Sentinel
import redis


def create_sentinel_redis(config):
    logger.info('start to connect sentinel redis: host-port:%s, db: %s' % (config['host-pot'], config['db']))
    host_port = parse_host(config["host-port"])
    sentinel = Sentinel(host_port, socket_timeout=2, password=config['pwd'],db=config['db'])
    master = sentinel.master_for('mymaster', socket_timeout=5)
    slave = sentinel.slave_for('mymaster', socket_timeout=2)
    return master, slave


def create_default_redis(config):
    """
    @attention: 创建一个默认的redis环境
    """
    logger.info("start to connect default redis: host-port: %s, db: %s" % (config['host-port'], config['db']))
    host_port = parse_host(config["host-port"])[0]
    connect = redis.StrictRedis( host=host_port[0], port=host_port[1], db=config["db"], password=config["pwd"])
    return connect


def parse_host(val):
    """
    @attention: 分解host,把10.1.113.158:26379分割为("10.1.113.158",26379)
    """
    info = re.findall(r"([\d\.]+):(\d+)", val)
    return [(item[0], int(item[1])) for item in info]


if __name__ == '__main__':
    a = "10.1.113.158:26379"
    print(parse_host(a))
