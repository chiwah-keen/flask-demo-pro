"""
Created on 2019年1月15日

@author: ljbai
"""
from utils.mongodb import MongoManager
import conf

mongo_cli = MongoManager(conf.MONGODB_CONNECT_URL, conf.MONGODB_DB)