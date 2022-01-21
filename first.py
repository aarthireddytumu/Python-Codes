# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
C:\Users\aarthi.reddy.tumu\.spyder-py3s
"""

#printfunction
print("Hello World!")
#to get input
a = input() #it takes string as input
#to get integer input
b = int(input("Enter the no:"))

#typeconversion
#implicit
x,y = 10,10.6
print("x is of type",type(x))
print("y is of type",type(y))
#to cnvrt int to float implicitly
x = x+y
print(x,type(x))

#explicit
s,t = "198",190.8
#to cnvrt str to int
s = int(s)
t = int(t)
print(type(s),type(t))
#to cnvrt value to bool
s = bool(s)
print(type(s))
#if you try to cnvrt str to int it will throw error , so we will be using ord func to assign ascii values based on character
#ordfunc
alp = "a"
alp = ord(alp)
print(alp,type(alp))
#hexfunc & octfunc
c = 56
c = oct(56)
d = hex(56)
print(c,d)
#base2func(binary)
ba = "10010"
ba = int(ba,2)
print(ba,type(ba))

#updatingavar
a = 7
a = a + 1
#or
a += 1 #shorthand operator

#random
import random
die_roll = random.randint(1,6)
if die_roll == 1:
    print("1")
elif die_roll == 2 or die_roll == 3:
    print("2/3")
else:
    print("4/5/6")


