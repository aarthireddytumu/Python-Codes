# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 11:17:57 2021

@author: aarthi.reddy.tumu
"""

'''List Data Structure #same type or differnent data types'''

#inbuilt data types
#ordered
#changeable
#allow duplicates
l1 = ["abc",34,True,34.5,"male"]

print(len(l1))
print(l1, type(l1))
#Indexing
print(l1[0])
print(l1[1])
print(l1[2])
print(l1[3])
print(l1[4])#
for i in l1:
 print(i)
for i in range(len(l1)):
 print(i,l1[i])
n = len(l1)
for i in range(1,n+1):
 print(l1[-i])
#
#slicing:
fruits = ["apple","banana","cherry","orange","kiwi","melon","pomo","papaya","mango"]
print(len(fruits))
print(fruits[:6])
print(fruits[::2])
print(fruits[::-1])
print(fruits[-4:-1])
#Index
print(fruits.index("pomo"))
print(fruits[6])#in or not in
print("kiwi" not in fruits)
#add only one items, at last only
fruits.append("fig")
fruits.insert(2,["a","b","c"])
print(fruits[2][2])
fruits[1]="Banana" # updating

print(fruits)
#remove, pop#
fruits.remove("Banana")
print(fruits)
fruits.pop(4)
print(fruits)
l1 = [1,2,3]
l2= [4,5,6]
l1.extend(l2)
print(l1)
l1 = l1 + l2
print(l1)
l1.clear()
#del l1 - deletes entire list
print(l1)

#inserting list to another list at a specified index
a = ['a','b','c']
b = ['d','e','f']
a[1:1] = b
print(a)
#inserting as a nested list
c = [3,6,5]
a[1] = c
print(a)

