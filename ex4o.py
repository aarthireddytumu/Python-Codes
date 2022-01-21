# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 21:17:00 2021

@author: aarthi.reddy.tumu
"""

#1
#c=0
#re = open(r"C:\Users\aarthi.reddy.tumu\OneDrive - Accenture\Desktop\test.txt","r")
#wr = open(r"C:\Users\aarthi.reddy.tumu\OneDrive - Accenture\Desktop\newtest.txt","a")
#for line in re:
#    c+=1
#    if c!=5:
#        wr.write(line)


#2
#re = open(r"C:\Users\aarthi.reddy.tumu\OneDrive - Accenture\Desktop\test.txt","r")
#wr = open(r"C:\Users\aarthi.reddy.tumu\OneDrive - Accenture\Desktop\newtest.txt","a")
#lines = re.readlines()
#for i in range(1,11):
#    wr.write(lines[i*-1])


##3
#import csv
#f = open(r"C:\Users\aarthi.reddy.tumu\OneDrive - Accenture\Desktop\test.csv","w",newline="")
#wr = csv.writer(f)
#wr.writerow(["ID","Name","age"])
#wr.writerow([123,"Amit",22])
#wr.writerow([124,"bob",21])
#f.close()

#4
re = open(r"C:\Users\aarthi.reddy.tumu\OneDrive - Accenture\Desktop\test.docx","r")
wr = open(r"C:\Users\aarthi.reddy.tumu\OneDrive - Accenture\Desktop\newtest.docx","a")
for line in re:
    wr.write(line)
    