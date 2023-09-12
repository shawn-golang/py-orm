'''
Author: psq
Date: 2021-04-28 16:21:01
LastEditors: psq
LastEditTime: 2023-09-12 11:22:55
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 
import  sys
import  time
sys.path.append('./')

import  configparser

from utils.databases.oracle.connector import cxconnection
from utils.databases.oracle.builder   import queryconstruction
from utils.databases.oracle.builder   import executeconstruction

cfg = configparser.ConfigParser()
cfg.read('./config/db.conf', encoding = 'utf-8')

class construct(object):

    def __init__(self, env):

        self.starttime = int(time.time())
        
        self.db = cxconnection.Connect(cfg, env)
        
    def select(self, **parameter):

        return self.db.querySQL(self.__sql(queryconstruction.Construction(parameter).sql))

    def insert(self, **parameter):

        return self.db.executeSQL(self.__sql(executeconstruction.Construction(parameter).sql))
        
    def insertall(self, **parameter):

        self.__sql(executeconstruction.Construction(parameter).sql)
        
        return self.db.executeSQL(self.__sql(executeconstruction.Construction(parameter).sql))

    def update(self, **parameter):

        return self.db.executeSQL(self.__sql(executeconstruction.Construction(parameter).sql))

    def delete(self, **parameter):
        
        return self.db.executeSQL(self.__sql(executeconstruction.Construction(parameter).sql))

    def query(self, **parameter):

        return self.db.querySQL(self.__sql(parameter['sql']))

    def execute(self, **parameter):

        return self.db.executeSQL(self.__sql(parameter['sql']))

    def __sql(self, sql):
        
        self.sql = sql

        return self.sql

    def __del__(self):

        log = [
            '[DB类型]: oracle',
			'[开始时间]: ' + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.starttime))),
			'[结束时间]: '	+ str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))),
			'[运行耗时/秒]: ' + str(int(time.time()) - self.starttime),
			'[SQL语句]: ' + self.sql
        ]






