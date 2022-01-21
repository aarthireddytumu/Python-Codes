# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 12:45:29 2021

@author: aarthi.reddy.tumu
"""

"""#Exception Handling:#try block
#Except
#finally'
a = 12
s = "hello"
print(a+s)
a =12
s = "hello"
try:
 a.append(s)
#will raise TypeError
except AttributeError:
 a = a + 1
 print(a)
except:
 print(str(a)+s)"""


"""try:
    if(3+4-5)<0:
        a = 3
        a.append("hello") 
# attribute error
    else:
        print("hello"+"4") 
# TypeError
except Exception as e:
    print("Error occured",e)"""

x = 5
for i in range(10):
    print(x)
    x-=1
    if x < 0:
        raise Exception("sorry , value is below zero")
        break

