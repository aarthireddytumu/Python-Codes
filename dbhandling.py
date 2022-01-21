# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:40:27 2021

@author: aarthi.reddy.tumu
"""


#Database Handling:#create Connection:
import sqlite3
con = sqlite3.connect("emp.db")
cursor = con.cursor()
#
cursor.execute("insert into employee values(9,'hello','qa')")
cursor.execute("update employee set empName = 'AarthiReddy' where empid = 3")
cursor.execute("delete from employee where empid = 122")
con.commit()
cursor.execute("select * from employee")
data = cursor.fetchall()
data = cursor.fetchone()
data = cursor.fetchmany(2)
print(data)

