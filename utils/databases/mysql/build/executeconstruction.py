#!/usr/bin/python
# -*- coding: UTF-8 -*-
import traceback

class Construction(object):
    
    def __init__(self, parameter:any):

        sqllist = {
            'insert'    :   'insert into',
            'insertall' :   'insert into',
            'update'    :   'update',
            'delete'    :   'delete from'
        }

        self.parameter = parameter

        self.f = traceback.extract_stack()[-2][2]

        self.sql = sqllist[self.f]

        self.__table(self.parameter['table'])

        self.__values(self.parameter['values'] if self.parameter.__contains__('values') else None)
        
        self.__where(self.parameter['where'] if self.parameter.__contains__('where') else None)

    def __table(self, table):
    
        self.sql += f" {table}"

    def __values(self, values):
    
        if self.f == "insert":

            self.sql += f"({str(', '.join(list(values.keys())))}) values ({self.__setVal(values)})"

        if self.f == "insertall":
            
            self.sql += f"({str(', '.join(list(values[0].keys())))}) values "
      
            for x in range(len(values)):
                
                self.sql += f"({self.__setVal(values[x])})"

                if len(values) > int(x + 1): 
                    
                    self.sql += ', '

        if self.f == 'update':

            self.sql += " set "

            if len(values) == 1:
                
                key = list(values.keys())[0]
                
                if isinstance(str(values[key]), str):
                    
                    self.sql += f"{str(key)} = '{str(values[key])}'" 
                    
                else:
                    
                    self.sql += str(values[key])

            else:

                for x in range(len(values)):
                    
                    key = list(values.keys())[x]

                    self.sql += f"{key} = "
                    
                    if isinstance(values[key], str):
                        
                        self.sql +=  f"'{values[key]}' " 
                    
                    else:
                    
                        self.sql += str(values[key])

                    if len(values) > int(x + 1): 
                        
                        self.sql += ', '

    def __where(self, where):

        if where == None: return

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


    def __setVal(self, values):
        
        v = list(values.values())

        result = ""

        for x in range(len(v)):

            if isinstance(v[x], str) and v[x][:7] != 'to_date':
            
                result += f"'{v[x]}'"
            
            else:
                
                result += str(v[x])

            if len(v) > int(x + 1):
                
                result += ','

        return result