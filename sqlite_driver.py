#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 4:34 PM
# @Author  : Steven
# @Contact : 523348709@qq.com
# @Site    : 
# @File    : sqlite_driver.py
# @Software: PyCharm
# -*- coding:utf-8 -*-

import sqlite3

class Sqlite_db():
    def __init__(self):
        #数据库名字
        self.db_name ='test.sqlite'

        self.conn=sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()

        #mysql列名
        #self.mysql_bar='url,title,time_line,tag,author,head,body'
        self.mysql_col_num=8

        mysql_col = []
        for i in range(0,self.mysql_col_num):
            mysql_col.append('?')
        self.mysql_col=','.join(mysql_col)

    #返回列数
    def get_col_num(self,table):
        self.cur.execute('select * from %s'%table)
        col_list=[tuple[0] for tuple in self.cur.description]
        return len(col_list)

    #返回所有列名
    def get_col_list(self,table):
        self.cur.execute('select * from %s' % table)
        col_list = [tuple[0] for tuple in self.cur.description]
        return col_list

    #执行insert语句时，返回新插入行的ID
    def insert_id(self):
        return self.cur.lastrowid()

    #当执行语句时，返回受影响的行数
    def affected_rows(self):
        pass

    #上次一查询语句的地方
    def last_query(self):
        pass

    #获取数据表总行数
    def count_all(self,table):
        self.cur.execute('select * from %s'%table)
        return len(self.cur.fetchall())

    #执行select语句，获取表的所有数据
    def get(self,table):
        self.cur.execute('select * from %s' % table)
        return self.cur.fetchall()

    def get_where(self,table,**data):
        #
        # for a, b in data.items():  # a 代表键 ，b代表值
        #     print data.items()
        items= data.items()
        list=[]
        for a,b in items:
            list.append('%s=%s'%(a,b))
        where= ' and '.join(list)

        sql='select * from %s where %s'%(table,where)
        print sql

        self.cur.execute('select * from %s where ?'%table,(where,))



    def add(self,table,*data):
        sql = 'insert into %s values(NUll,%s)' % (table,self.mysql_col)
        #print sql
        self.cur.execute(sql, data)
        self.conn.commit()

    def test(self,*data):
        pass
        #print self.conn.


    def get_all(self,table):
        sql='select * from %s'%table
        self.cur.execute(sql)
        value=self.cur.fetchall()
        print value

    def get_last_one(self,table,col_name):
        sql='select %s from %s order by ID DESC limit 1'%(col_name,table)
        self.cur.execute(sql)
        result=self.cur.fetchone()
        return result[0]

if __name__ == '__main__':

    sqlite=Sqlite_db()
    dic={'id': 1, 'a': 'siu'}
    print sqlite.get_where('test',**dic)

