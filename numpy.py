# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 11:04:42 2021

@author: aarthi.reddy.tumu
"""

#Numpy
#Arrays
import numpy as np
l1 = [10,20,30,40,50]
arr = np.array(l1)
print(l1,"\n",arr,"\n",type(arr))
#ones and zeros:
#
arr1 = np.ones((3,5,4),dtype = float)
arr1 = np.zeros((3,5,4))
print(arr1)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
#arange:
arr2 = np.arange(5,21)
print(arr2)
arr2 = np.arange(1,25,4,dtype = float)
print(arr2)
arr2 = np.linspace(1,25,100)
print(arr2)
#reshape
one_d = np.arange(1,31)
two_d = one_d.reshape(5,6)
three_d = one_d.reshape(3,2,5)

print(one_d,"\n",two_d,"\n",three_d)

print(len(one_d))
print(len(two_d))
print(len(three_d))
arr3 = np.arange(1,29).reshape(4,7)
print(arr3[1:3,2:5])

arr4 = np.arange(1,31).reshape(2,5,3)
print(arr4[:,2:4,:])
#ndarray:
arr4 = np.ndarray((5,3),dtype = float)
print(arr4)
#random.randint
arr4 = np.random.randint(50,100,size=150)
print(arr4.std())

