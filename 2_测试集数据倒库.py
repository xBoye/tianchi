# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 20:48:59 2018
@title：天池大数据竞赛-测试集数据倒库
@author: ff7f
"""
import os
from db import DB

dbDir = 'db'
if not os.path.exists(dbDir):
    os.mkdir(dbDir)

# 创建和连接数据库
dbname = 'db\\tianchi2018.db'
if os.path.exists(dbname):
    print(f'>>> [{dbname}]数据库已存在！')
    #os.remove(dbname)

# 连接数据库，不存在的话自动创建
db = DB(dbname)

# 删除表
drop_table_prefix = "drop table if exists prefix"
drop_table_querypred = "drop table if exists querypred"

#db.cur.execute(drop_table_prefix)
#db.cur.execute(drop_table_querypred)

# 创建table
create_table_prefix = """  
create table if not exists prefix(      # 搜索词前缀表
    id      smallint,
    prefix  char(20),
    title   char(20),
    tag     char(10),
    label   tinyint)"""

create_table_querypred = """
create table if not exists querypred(   # 查询预测表
    id      integer primary key autoincrement,
    pid     smallint,
    title   char(20),
    rate    float)"""

db.cur.execute(create_table_prefix)
db.cur.execute(create_table_querypred)

# 插入记录
sql_insert_prefix = "insert into prefix(id, prefix, title, tag) values(?,?,?,?)"
sql_insert_querypred = " insert into querypred(pid, title, rate) values(?,?,?)"

testfile = 'data\\oppo_round1_test_A_20180929.txt'   # 测试集 16M 5万条未标注数据
with open(testfile, encoding='utf8') as f:
    data = f.read().strip('\n').split('\n')

for n,r in enumerate(data):
    t = r.split('\t')
    print(t)
    t_prefix = (n+1, t[0], t[2],t[3])
    print(t_prefix)
    db.insert(sql_insert_prefix,t_prefix)
    for title,rate in eval(t[1]).items():
        t_pred = (n+1, title, float(rate))
        print(t_pred)
        db.insert(sql_insert_querypred, t_pred)
    
db.close()