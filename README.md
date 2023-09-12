# py-orm


[数据库操作类]

# 支持语句如下

# [select]				查询

# [update]				修改

# [delete]				删除

# [insert] 				添加

# [insertall]				批量添加

# [query]					自定义读语句

# [execute]				自定义写语句

# [XAtransaction]			分布式跨库事务

# 调用示例：

    from    utils.databases.mysql import mysql

    db = mysql.construct(env = 'test')

# [XAtransaction]

    [参数]
			[env]		参与事务的实例	 list
			[sql]			sql写语句		dist

    [示例]
				db.XAtransaction(
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
				# 目前仅支持mysql
				# 参与事务的数据表必须为innodb存储引擎
				# env内所有参与事务的示例必须有配套的写入语句，否则会导致事务整体回滚！！！
				# 如果两个库在同一个连接实例时会导致调用报错！！！

    [返回结果]
				布尔对象

# [query]

    [参数]
				[sql]			sql读语句		string

    [示例]

    db.query(
			        sql = 'select test_id from test'
			    )

    [返回结果]
				list对象

# [execute]

    [参数]
				[sql]			*sql写语句						  sting
				[autocommit]	自动提交[默认: True]			   bool

    [示例]

    db.execute(
			        sql = 'insert into test (test_id) values (23)'
			    )

    [返回结果]
				布尔对象

# [select]

    [参数]
				[table]		数据表名		string
				[alias]		设置别名 		string
				[where]		查询条件		dist
				[fields]	限定字段		list
				[orderby]	排序方式		string
				[limit]		数据分页		list
				[join]		关联查询		list
					{
						'connect':  连接方式['left', 'right', 'inner'],
	                	'alias':    别名,
	                	'table':    关联数据表,
	                	'on':   	关联字段
					}

    [示例]
				db.select(
			        table   =   'test',
			        alias   =   'u',
			        where   =   {'u.xxx': 'xxx', 'u.xxx': 'xxx'},
			        fields  =   ['u.xxx', 'a.xxx', 't.xxx'],
			        orderby =   'u.xxx asc',
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

    [返回结果]
				list对象

# [update]

    [参数]
				[table]			数据表名						    string
				[where]			操作条件						    dist
				[values]		操作字段							dist
				[autocommit]	自动提交[默认: True]		   	     bool

    [示例]

    db.update(
			        table   =   'test',
			        values  =   {'test_name': 2},
			        where   =   {'test_id': 1}
			    )

    [返回结果]
				布尔对象

# [insert]

    [参数]
				[table]			数据表名							string
				[values]			操作字段							dist
				[autocommit]		自动提交[默认: True]		   		bool

    [示例]
				db.insert(
			        table   =   'test',
			        values  =   {'test_id': 21, 'test_name': 1, 'test_value': 1, 'test_age': 1}
			    )

    [返回结果]
				布尔对象

# [insertall]

    [参数]
				[table]			数据表名							string
				[values]		操作字段							list
				[autocommit]	自动提交[默认: True]		  		 bool

    [示例]

    db.insertall(
			        table   =   'test',
			        values  =   [
			            {'test_id': 22, 'test_name': 1, 'test_value': 1, 'test_age': 1},
			            {'test_id': 23, 'test_name': 1, 'test_value': 1, 'test_age': 1}
			        ]
			    )

    [返回结果]
				布尔对象
