# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:14:44 2021

@author: aarthi.reddy.tumu
"""


#def smart_div(func):
#    def inner(a,b):
#        if a < b:
#            a,b = b,a
#        return func(a,b)
#    return inner
#
#@smart_div
#def div(a,b):
# print(a/b)
#
#div(2,4)

def uppercase_decorator(func):
    def inner():
        a = func()
        output=a.upper()
        return output
    return inner
def split_decorator(func):
    def inner():
        b = func()
        op1 = b.split()
        return op1
    return inner

@split_decorator
@uppercase_decorator
def say_hi():
    return "hello there"
print(say_hi())

