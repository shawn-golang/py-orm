'''
Author: psq
Date: 2021-04-28 16:21:01
LastEditors: psq
LastEditTime: 2023-09-12 10:52:59
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
from ast import Try
import  sys
import  time
import  pymysql

sys.path.append('./')


class Connect():

    def __init__(self, env:any):

        self.starttime = int(round(time.time() * 1000))

        try:
            
            self.db  = pymysql.connect(
                port     = int(env['port']),
                host     = str(env['host']),
                user     = str(env['user']),
                charset  = str(env['charset']),
                password = str(env['password']),
                db       = str(env['db']),
            )

        except Exception as e:

            raise RuntimeError('connectErr:', e)

        self.cursor = self.db.cursor(cursor = pymysql.cursors.DictCursor)

    def querySQL(self, sql:str) -> tuple:

        try:
            
            self.cursor.execute(self.__sql(sql))

            self.result = True

        except Exception as e:

            self.result = False
            
            raise RuntimeError('executeErr:', e)
        
        # 操作日志，可以根据自己的方式保存下来
        log = {
            "dbType":       "mysql",
            "startTime":    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.starttime / 1000)),
            "endTime":      time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time()))),
            "runResult":    self.result,
            "runTime":      (int(round(time.time() * 1000)) - self.starttime) / 1000,
            "sql":          self.sql
        }

        return self.cursor.fetchall()

    def executeSQL(self, sql:str, autocommit:bool) -> bool:

        try:

            self.cursor.execute(self.__sql(sql))

            if autocommit: self.db.commit()

            self.result = True

        except Exception as e:
            
            if autocommit: self.db.rollback()
  
            self.result = False
        
        # 操作日志，可以根据自己的方式保存下来
        log = {
            "logType":      "DBLogs",
            "dbType":       "mysql",
            "startTime":    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.starttime / 1000)),
            "endTime":      time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time()))),
            "runResult":    self.result,
            "runTime":      (int(round(time.time() * 1000)) - self.starttime) / 1000,
            "sql":          self.sql
        }

        return self.result
    
    def __sql(self, sql):
        
        self.sql = sql

        return self.sql

    def __del__(self):

        try:
            
            self.db.close
        
        except Exception as e:
            ...