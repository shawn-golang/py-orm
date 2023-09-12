#!/usr/bin/python
# -*- coding: UTF-8 -*-

import  sys
import  uuid
import  json
sys.path.append('./')

from utils.databases.mysql.connect  import pyconnection
from utils.databases.mysql.build    import queryconstruction
from utils.databases.mysql.build    import executeconstruction

class construct(object):

    def __init__(self, env:str):
        
        with open("./config/db.json", "r") as f:

            f = json.load(f)[env]
        
        self.db = pyconnection.Connect(env = f)

    '''
    description: 数据查询
    param {*} self
    param {object} parameter
    return {*}
    '''    
    def select(self, **parameter:any) -> bool:

        return self.db.querySQL(queryconstruction.Construction(parameter).sql)

    '''
    description: 数据写入
    param {*} self
    param {object} parameter
    return {*}
    '''    
    def insert(self, **parameter:any) -> bool:
    
        return self.db.executeSQL(
            sql         = executeconstruction.Construction(parameter).sql,
            autocommit  = parameter['autocommit'] if parameter.__contains__('autocommit') else True
        )

    '''
    description: 批量数据写入
    param {*} self
    param {object} parameter
    return {*}
    '''    
    def insertall(self, **parameter:any) -> bool:

        return self.db.executeSQL(
            sql         = executeconstruction.Construction(parameter).sql,
            autocommit  = parameter['autocommit'] if parameter.__contains__('autocommit') else True
        )

    '''
    description: 数据修改
    param {*} self
    param {object} parameter
    return {*}
    '''    
    def update(self, **parameter:any) -> bool:

        return self.db.executeSQL(
            sql         = executeconstruction.Construction(parameter).sql,
            autocommit  = parameter['autocommit'] if parameter.__contains__('autocommit') else True
        )

    '''
    description: 数据删除
    param {*} self
    param {object} parameter
    return {*}
    '''    
    def delete(self, **parameter:any) -> bool:

        return self.db.executeSQL(
            sql         = executeconstruction.Construction(parameter).sql,
            autocommit  = parameter['autocommit'] if parameter.__contains__('autocommit') else True
        )

    '''
    description: 自定义读语句
    param {*} self
    param {object} parameter
    return {*}
    '''    
    def query(self, **parameter:any) -> bool:

        return self.db.querySQL(parameter['sql'])

    '''
    description: 自定义写语句
    param {*} self
    param {object} parameter
    return {*}
    '''    
    def execute(self, **parameter:any) -> bool:
        
        return self.db.executeSQL(
            sql         = parameter['sql'],
            autocommit  = parameter['autocommit'] if parameter.__contains__('autocommit') else True
        )
    
    '''
    description: 分布式跨库事务
    param {*} self
    param {object} parameter
    return {*}
    '''    
    def XAtransaction(self, **parameter:any) -> bool:
        
        transactionID, sqlResult  = uuid.uuid1(), []

        for x in range(len(parameter['env'])):

            self.__init__(parameter['env'][x])
            
            self.query(sql = f"xa start '{transactionID}';")
            
            for s in range(len(parameter['sql'][parameter['env'][x]])):
            
                sqlResult.append(self.execute(
                    sql         =   parameter['sql'][parameter['env'][x]][s],
                    autocommit  =   False 
                ))
 
            self.query(sql = f"xa end '{transactionID}';")
            self.query(sql = f"xa prepare '{transactionID}';")

        for x in range(len(parameter['env'])):

            self.__init__(parameter['env'][x])
            
            if False in sqlResult:

                self.query(sql =  f"xa rollback '{transactionID}';")
            else:

                self.query(sql = f"xa commit '{transactionID}';")

        return False if False in sqlResult else True
    
    














