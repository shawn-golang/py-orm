#!/usr/bin/python
# -*- coding: UTF-8 -*-
import traceback

class Construction(object):
    
    def __init__(self, parameter):

        sqllist = {
            'insert'    :   'insert into',
            'insertall' :   'insert all',
            'update'    :   'update',
            'delete'    :   'delete from'
        }

        self.parameter = parameter

        self.f = traceback.extract_stack()[-2][2]

        self.sql = sqllist[self.f]

        self.__values(self.parameter['values'] if self.parameter.__contains__('values') else None)
        
        self.__where(self.parameter['where'] if self.parameter.__contains__('where') else None)

    def __table(self, table):
    
        self.sql += ' ' + table

    def __values(self, values):
    
        if self.f == 'insert':

            self.__table(self.parameter['table'])

            self.sql += "("+ str(', '.join(list(values.keys())))+ ") values (" + self.__setVal(values) + ")"

        if self.f == 'insertall':
            
            for x in range(len(values)):
            
                self.sql += " into " + str(self.parameter['table']) + "("+ str(', '.join(list(values[x].keys())))+ ") values ("+self.__setVal(values[x])+")"

            self.sql += " select count(*) from " + self.parameter['table']

        if self.f == 'update':
            
            self.__table(self.parameter['table'])

            self.sql += " set "

            if len(values) == 1:
                
                key = list(values.keys())[0]

                self.sql += str(key) + " = " + "'" + str(values[key]) + "'" if isinstance(str(values[key]), str) else str(values[key])

            else:

                for x in range(len(values)):

                    key = list(values.keys())[x]
                    v = list(values.values())

                    self.sql += key + ' = '

                    self.sql +=  "'" + values[key] + "' " if isinstance(values[key], str) and v[x][:7] != 'to_date' else str(values[key])

                    if len(values) > int(x + 1):
                        self.sql += ', '

        if self.f == 'delete':

            self.__table(self.parameter['table'])



    def __where(self, where):

        if where == None: return

        if isinstance(where, str) :
            
            self.sql += " where " + where

        else:

            self.sql += " where ("

            for x in range(len(where)):

                self.sql += str(list(where.keys())[x]) + " = '" + str(list(where.values())[x]) + "'"

                self.sql += ") " if x == int(len(where)) - 1 else " and "


    def __setVal(self, values):
        
        v = list(values.values())

        result = ""

        for x in range(len(v)):

            result += "'" + v[x] + "'" if isinstance(v[x], str) and v[x][:7] != 'to_date' else str(v[x])

            if len(v) > int(x + 1):
                result += ','

        return result