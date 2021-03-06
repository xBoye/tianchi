# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 22:01:57 2018
@title：数据库类DB
@author: ff7f
"""

import sqlite3
import os
#import re

class DB:
    # DB类
    def __init__(self, dbname):
        
        #assert os.path.exists(dbname), f'数据库[{dbname}]不存在！' 
        self.dbname = dbname
        self.con = None
        self.cur = None
        
        self.open()
        
    def open(self):
        self.con = sqlite3.connect(self.dbname)
        self.cur = self.con.cursor()
    
    
    def insert(self, sql, args=None, R=None):
        # 插入
        assert args, 'None data!'
        if R:
            self.cur.execute(sql % R, args)
        else:
            self.cur.execute(sql, args)
    
    def select(self, sql, args=None):
        if args:
            self.cur.execute(sql % args)
        else:
            self.cur.execute(sql)
        #result = '\n'.join(map(repr,self.cur.fetchall()))
        """
        result = []
        for row in self.cur.fetchall():
            tup = []
            for item in row:
                if item:
                    tup.append(item)
            result.append(tuple(tup))
        result = '\n'.join(map(repr, result))
        #print(result.replace("'",''))
        """
        #result = repr(self.cur.fetchall()).replace("'",'')
        result = set(self.cur.fetchall())
        #print(result)
        return result
        
    def close(self):
        self.cur.close()
        self.con.commit()
        self.con.close()

# main
if __name__ == '__main__':
    sql_insert = "insert into %s values(?,?,?)"
    dbname = 'test.db'
    if os.path.exists(dbname):
        os.remove(dbname)
    db = DB(dbname)
    # 创建表SQL命令
    create_table_R = 'create table if not exists R(A int(1),B int(1),C int(1))'
    create_table_S = 'create table if not exists S(A int(1),B int(1),C int(1))'
    # 创建R，S
    db.cur.execute(create_table_R)
    db.cur.execute(create_table_S)
    
    # 往表R,S插入数据
    sql_insert = """insert into %s values(?,?,?)"""
    r = [(3,6,7),(2,5,7),(7,2,3),(4,4,3)]
    s = [(3,4,5),(7,2,3)]
    
    for t in r:
        db.insert(sql_insert, t, 'R')
    for t in s:
        db.insert(sql_insert, t, 'S')

    db.close()