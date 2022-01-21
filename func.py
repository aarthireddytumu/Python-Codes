# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 16:12:43 2021

@author: aarthi.reddy.tumu
"""

#Fucntions
def hello(): # function definition
 return "hello all"

print(hello()) 
# calling the function#
def add(a,b):
 c = a + b
 print(c)

add(4,6)
def my_func(*kids): 
#arbitary argument
 print("The youngest child is " ,kids[1])

my_func("bob","peter")

def my_func(*emp_details):
 print("the name is ",emp_details[0])
 print("the id is ",emp_details[1])

my_func("msk",123)
#
def my_func(name,id,age):
    #keyword arguments
 print("the name is ",name,"\nthe id is ",id,"\nthe age is ",age)

my_func(id = 123,age=22,name = "msk")
#Arbitary keyword agrguments: **kwargs
def my_func(**kid):
 print("The first name is " + kid["fname"])

my_func(lname = "parr",fname="bob")
#Default parameter value
def my_func(country="India"):
 print("I am from "+country)

my_func("sweden")
my_func("Canada")
my_func("India")
my_func()


def add(a,b = 5):
 c = a + b
 print(c)
 
add(4)

def add(a,b = None):
 print(b)
 
add(4)

