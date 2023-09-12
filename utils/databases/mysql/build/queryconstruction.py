'''
Author: psq
Date: 2023-06-29 18:09:52
LastEditors: psq
LastEditTime: 2023-09-12 11:02:09
'''
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
        
        self.sql += f" as {alias}" if alias != None else ''

    def __join(self, join):

        for x in range(len(join)):
            
            j = join[x]['connect'].lower() if join[x].__contains__('connect') else 'left';

            try:
                
                self.sql += f" {j} join {join[x]['table']} as {join[x]['alias']} on {join[x]['on']}"

            except Exception as e:
                
                RuntimeError('executeErr:', e)

    def __where(self, where):

        if where != None:

            if isinstance(where, str) :
                
                self.sql += f" where {where}"

            else:

                self.sql += " where ("

                for x in range(len(where)):

                    self.sql += f"{str(list(where.keys())[x])} = '{str(list(where.values())[x])}'"

                    if x == int(len(where)) - 1:

                        self.sql += ") " 
                        
                    else:
                        
                        self.sql += " and "

    def __limit(self, limit):

        if limit != None:
            
            if len(limit) == 1:
            
                self.sql += f"limit {str(limit[0])}"
            
            else:
                
                self.sql += f"limit {str(int(limit[0]) * int(limit[1])) + ',' + str(limit[0])}"

    def __table(self, table):

        self.sql += f"from {table}"

    def __fields(self, fields):
        
        if type(fields) != str:

            self.sql += ','.join(fields) + ' ' 
        
        else:
            
            self.sql += fields + ' '

    def __orderby(self, orderby):
        
        if orderby != None:
            
            self.sql += f"order by  {str(orderby)}"
            
        else:
            
            self.sql += ' '

    def __group(self, group):
        pass

    def __having(self, having):
        pass