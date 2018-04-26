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
        self.conn=sqlite3.connect('secrss.sqlite')
        self.cur=self.conn.cursor()
        #mysql列名
        #self.mysql_bar='url,title,time_line,tag,author,head,body'
        self.mysql_col_num=8
        mysql_col = []
        for i in range(0,self.mysql_col_num):
            mysql_col.append('?')
        self.mysql_col=','.join(mysql_col)


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

