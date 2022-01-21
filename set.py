# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 14:44:10 2021

@author: aarthi.reddy.tumu
"""

#Set
#unordered
#unindexed
#curly brackets
#no duplicates allowed
#unchageable
#you cannot change the items, but it allows to add new items
set1 = {"apple","banana","cherry",34,True}
print(set1, type(set1))
#
for i in set1:
    print(i)
#
"banana" in set1
set1.add("orange")
print(set1)

veg = ["carrot","tomato","potato"]
set1.update(veg)
print(set1)

set1.discard("banana")   #-   you can use set1.remove("banana") to remove banana
set1.discard("kiwi")    #-      you cannot use set1.remove("kiwi"), bcoz it throws an error since it is not present in the list
set1.pop()
set1.pop()
print(set1)
s1 = {"a","b","c","d"}
s2= {1,2,3}
s3=s1.union(s2)
print(s3)
s1.update(s2)
print(s1)

#intersection, intersection_update
x = {"apple","banana","cherry"}
y={"google","microsoft","apple"}

s = x.intersection(y)
print(s)

x.intersection_update(y)
print(x)
#symmetric difference , symmetric difference update
x.symmetric_difference_update(y)
print(x)

