#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
import  sys
import  time
import  json
sys.path.append('./')

import  cx_Oracle
import  configparser
cfg = configparser.ConfigParser()

class Connect(object):

    def __init__(self, cfg, env):

        try:

            self.db  = cx_Oracle.connect(
                cfg.get('oracle', env + '_user'),
                cfg.get('oracle', env + '_password'),
              	cfg.get('oracle', env + '_host') + ':' + cfg.get('oracle', env + '_port') + '/' + cfg.get('oracle', env + '_server')
            )

        except Exception as e:

            raise RuntimeError('connectErr:', e)
            return

        self.cursor = self.db.cursor()

    def __del__(self):
        
        self.cursor.close()
        self.db.close()

    def __muster(self, data, key):

        results = []

        for x in range(len(data)):
            
            l = {}

            for k in range(len(data[x])):
                
                l[key[k][0]] = data[x][k] 

            results.append(l)

        return results

    def querySQL(self, sql):
        
        try:
            
            self.cursor.execute(sql)

            return self.__muster(self.cursor.fetchall(), self.cursor.description)

        except Exception as e:

            raise RuntimeError('executeErr:', sql)

    def executeSQL(self, sql):

        try:

            self.cursor.execute(sql)

            self.db.commit()

            return True

        except Exception as e:

            self.db.rollback()

            return False





