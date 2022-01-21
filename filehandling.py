# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 09:08:14 2021

@author: aarthi.reddy.tumu
"""


#File Handling
#reading
#f = open("C:\Users\aarthi.reddy.tumu\.spyder-py3\python\strings.py","rt")
f = open("C:\\Users\\aarthi.reddy.tumu\\.spyder-py3\\python\\strings.py","r")
print(f.read(10))
print(f.readline())
print(f.readline())
#Read last line :
with open(r"C:\Users\aarthi.reddy.tumu\.spyder-py3\python\strings.py","r") as f:
 lines =f.readlines()
print(lines[5])

with open(r"C:\Users\aarthi.reddy.tumu\.spyder-py3\python\strings.py","r") as f:
 lines = f.readlines()

for i in range(1,6):
 print(lines[i*-1])

#Writing#-"a" -append
#-"w" -
f = open("abc.txt","a")
f.write("now the file has more content")
f.close()
f = open("abcd.txt","w")
f.write("now the file has more content")
f.close()

#f = open("tee.txt","x")
with open("abc.txt","w") as f:
 line1 = "Hello world"
 line2 = "Good Morning"
 print("finished")
 f.writelines([line1,line2])
 f.write("{}\n{}\n".format(line1,line2))
import os
if os.path.exists("abcd.txt"):
 os.remove("abcd.txt")
 print("file removed")
else:
 print("The file does not exist")
import os
os.rmdir("t")

f = open(r"C:\Users\aarthi.reddy.tumu\.spyder-py3\python\strings.py","r")
data = f.readlines()
f.close
print(data)
data.insert(3,"Hi i am inserted ")
f = open(r"C:\Users\aarthi.reddy.tumu\.spyder-py3\python\strings.py","w")
data = "".join(data)
f.write(data)
f.close()



