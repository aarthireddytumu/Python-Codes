# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 21:54:20 2021

@author: aarthi.reddy.tumu
"""
#1
import sqlite3
con = sqlite3.connect("student.db")
cursor = con.cursor()

cursor.execute("insert into student values(101,'Leela','22')")
cursor.execute("insert into student values(102,'sheela','22')")
cursor.execute("insert into student values(103,'heela','22')")
cursor.execute("insert into student values(104,'shiny','22')")
cursor.execute("insert into student values(105,'kokkiee','22')")
data = cursor.fetchall()
print(data)
cursor.execute("update employee set Name = 'AarthiReddy',Age = 23 where empid = 103")
cursor.execute("delete from employee where empid = 122")
con.commit()
cursor.execute("select * from employee")
data = cursor.fetchall()
data = cursor.fetchone()
data = cursor.fetchmany(2)
print(data)