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
    def __init__(self,db_name):
        #数据库名字
        self.db_name =db_name

        self.conn=sqlite3.connect(self.db_name,check_same_thread=False)
        self.cur = self.conn.cursor()

        #mysql列名
        #self.mysql_bar='url,title,time_line,tag,author,head,body'
        self.mysql_col_num=6

        mysql_col = []
        for i in range(0,self.mysql_col_num):
            mysql_col.append('?')
        self.mysql_col=','.join(mysql_col)

    #返回一个包含所有数据库名称的列表
    def list_databases(self):
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        dbs = self.cur.fetchall()
        return dbs

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

    #获取数据表总行数
    def count_all(self,table):
        self.cur.execute('select * from %s'%table)
        return len(self.cur.fetchall())


    def get_where(self,table,**data):
        #
        # for a, b in data.items():  # a 代表键 ，b代表值
        #     print data.items()
        items= data.items()
        list=[]
        for a,b in items:

            list.append('%s="%s"'%(a,b))
        where= ' and '.join(list)

        sql="select * from '%s' where %s"%(table,where)
        self.cur.execute(sql)
        result= self.cur.fetchall()
        return result



    def add(self,table,*data):
        mysql_col = []
        for i in range(0, self.get_col_num(table)-1):
            mysql_col.append('?')
        mysql_col = ','.join(mysql_col)

        sql = 'insert into %s values(NUll,%s)' % (table,mysql_col)
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
        return value

    def get_all_limit(self,table,num):
        sql = 'select * from %s limit %d' % (table,num)
        self.cur.execute(sql)
        value = self.cur.fetchall()
        return value

    def get_last_one(self,table,col_name):
        sql='select %s from %s order by ID DESC limit 1'%(col_name,table)
        self.cur.execute(sql)
        result=self.cur.fetchone()
        return result[0]



if __name__ == '__main__':
    sql=Sqlite_db('movie.sqlite')
    print sql.get_where('6v_movie',href='http://www.hao6v.com/dy/2018-07-16/LangRenShenTan.html')

