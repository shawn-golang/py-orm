'''
Author: psq
Date: 2023-09-12 10:38:46
LastEditors: psq
LastEditTime: 2023-09-12 11:21:50
'''

from utils.databases.mysql    import  mysql
from utils.databases.oracle   import  oracle

if __name__ == '__main__':
    
    db = mysql.construct(env = 'mysql')
    
    '''
    description: 查询数据
    return {*}
    '''    
    select = db.select(
        table   =   'test', # 查询表名
        alias   =   'u', # 设置别名
        where   =   {'u.xxx': 'xxx', 'u.xxx': 'xxx'}, # 查询条件
        fields  =   ['u.xxx', 'a.xxx', 't.xxx'], # 限制输出字段
        orderby =   'u.xxx asc',    # 排序方式
        limit   =   [5, 1],	# 每页显示数量, 页码
        join    =   [
            {
                'connect':  'left', # 此项入不传则默认使用left连接
                'alias':    'a',
                'table':    'account',
                'on':   	'u.xxx = a.xxx'
            },
            {
                'connect':  'left', # 此项入不传则默认使用left连接
                'alias':    't',
                'table':    'account_tree',
                'on':   	'u.xxxx = t.xxx'
            }
        ],
    )
    
    print(select) # 返回list对象
    
    '''
    description: 修改数据
    return {*}
    '''    
    update = db.update(
        table   =   'test',
        values  =   {'test_name': 2},
        where   =   {'test_id': 1}
    )
    
    print(update) # 返回布尔对象
    
    '''
    description: 插入数据
    return {*}
    '''    
    insert = db.insert(
        table   =   'test',
        values  =   {'test_id': 21, 'test_name': 1, 'test_value': 1, 'test_age': 1}
    )
    
    print(insert) # 返回布尔对象
    
    '''
    description: 一次插入多条数据
    return {*}
    '''    
    insertall = db.insertall(
        table   =   'test',
        values  =   [
            {'test_id': 22, 'test_name': 1, 'test_value': 1, 'test_age': 1},
            {'test_id': 23, 'test_name': 1, 'test_value': 1, 'test_age': 1}
        ]
    )
    
    print(insertall) # 返回布尔对象
    
    '''
    description: 自定义读语句
    return {*}
    '''    
    query = db.query(
        sql = 'select test_id from test'
    )
    
    print(query) # 返回读语句
    
    '''
    description: 自定义写语句
    return {*}
    '''    
    execute = db.execute(
        sql = 'insert into test (test_id) values (23)'
    )
    
    print(execute) # 返回布尔对象
    
    '''
    description: 跨库事务
    return {*}
    '''    
    XAtransaction = db.XAtransaction(
        env     =   ['sit', 'sit2'],
        sql     =   {
            'sit':  [
                'insert into test_table_1 (tb_a) values ("1");',
                'insert into test_table_1 (tb_a) values ("2");'
            ],
            'sit2': [
                'insert into test_table_2 (tb_b) values ("3");',
                'insert into test_table_2 (tb_v) values ("4");',
                'insert into test_table_2 (tb_v) values ("5");'
            ]
        }
    )

    print(XAtransaction) # 返回布尔对象
    # 目前仅支持mysql !!!
    # 参与事务的数据表必须为innodb存储引擎 !!!
    # env内所有参与事务的示例必须有配套的写入语句，否则会导致事务整体回滚 ！！！
    # 如果两个库在同一个连接实例时会导致调用报错 ！！！