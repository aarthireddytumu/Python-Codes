# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:13:35 2021

@author: aarthi.reddy.tumu
"""

import csv
f = open("class.csv","r")
row = csv.reader(f)
next(row)
#skip one row
for i in row:
 print(i[1],i[2])

with open("class.csv","r")as f:
 row = csv.reader(f)
 l1 = list(row)
 print(l1[1],l1[3])
f = open("class.csv","r")
row = csv.DictReader(f,fieldnames=["Subjects","class"])
for i in row:
 print(i)
##writer Function:
f = open("class.csv","w",newline="")
wr = csv.writer(f)
wr.writerow(["Name","age","empid"])
wr.writerow(["Amit",22,123])
wr.writerow(["bob",21,124])
f.close()

fields = ["Name","age"]
rows =[{"Name":"lily","age":22},{"Name":"parr","age":21}]
f = open("class.csv","w",newline="")
wr = csv.DictWriter(f,fieldnames = fields)
wr.writeheader()
wr.writerows(rows)
f.close()

