#!/usr/bin/python
# -*- coding: UTF-8 -*-
import traceback

class Construction(object):
    
    def __init__(self, param):

        self.sql = traceback.extract_stack()[-2][2] + ' '

        self.__fields(param['fields'] if param.__contains__('fields') else '*')

        self.__table(param['table'])

        self.__alias(param['alias'] if param.__contains__('alias') else None)

        self.__join(param['join'] if param.__contains__('join') else [])
        
        self.__where(param['where'] if param.__contains__('where') else None)

        self.__orderby(param['orderby'] if param.__contains__('orderby') else None)

        self.__limit(param['limit'] if param.__contains__('limit') else None)

    def __alias(self, alias):
        
        self.sql += ' ' + alias if alias != None else ''

    def __join(self, join):

        for x in range(len(join)):
            
            f = join[x]['connect'].lower() if join[x].__contains__('connect') else 'left';

            try:
                
                self.sql += ' ' + f + ' join ' 
                self.sql += join[x]['table'] 
                self.sql += ' ' + join[x]['alias'] 
                self.sql += ' on ' + join[x]['ass']

            except Exception as e:
                
                RuntimeError('executeErr:', e)

    def __where(self, where):

        if where != None:

            if isinstance(where, str) :
                
                self.sql += " where " + where

            else:

                self.sql += " where ("

                for x in range(len(where)):

                    self.sql += str(list(where.keys())[x]) + " = '" + str(list(where.values())[x]) + "'"

                    self.sql += ") " if x == int(len(where)) - 1 else " and "

    def __limit(self, limit):

        if limit == None: return 

        pagestr = 'select * from (select oracle.*, rownum as numrow from ('

        if len(limit) == 1:
                
            self.sql = pagestr + self.sql + ') oracle)  where (numrow <= '+ str(limit[0]) +')'

        else:

            start = str(limit[1] - 1) if limit[1] == 1 else str(limit[0])

            end = str(limit[0] * limit[1])

            self.sql = pagestr + self.sql + ') oracle)  where (numrow > '+start +' and numrow <= '+ end +')'

    def __table(self, table):

        self.sql += 'from ' + table

    def __fields(self, fields):
        
        self.sql += ','.join(fields) + ' ' if type(fields) != str else fields + ' '

    def __orderby(self, orderby):
        
        self.sql += ' order by ' + str(orderby) + ' ' if orderby != None else ' '

    def __group(self, group):
        pass

    def __having(self, having):
        pass