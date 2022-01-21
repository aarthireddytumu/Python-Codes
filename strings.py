# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:28:32 2021

@author: aarthi.reddy.tumu
"""

a = '''Star Wars creator George Lucas had begun developing a live-action Star Wars television series by 2009,
 but this project was deemed too expensive to produce. He sold Lucasfilm to Disney in October 2012.
 Subsequently, work on a new Star Wars series began for Disney+. Favreau signed on in March 2018,
 serving as writer and showrunner. He executive produces alongside Dave Filoni, Kathleen Kennedy,
 and Colin Wilson. The series' title was announced in October 2018,
 with filming starting at Manhattan Beach Studios in California'''

a = a.replace("Star","Moon")
print(a)
print(a)
a = "Hello, World!."
print(a[4])
for i in a:
 print(i)
print(len(a))
txt = " The best things in life are free"
print("life" in txt)

print("!" in a)
print(a[::-1])
a = input("enter a string:")

reverse = a[::-1]

if a == reverse:
 print("The string is palindrome")
else:
 print("not a palindrome")
print(a.lower())

b = "#Good, Morning!#"
print(len(b))
#strip,lstrip,rstrip
b = b.strip("#")
print(b)
print(b.replace("G","W"))
#split
f ="Prevention# is better#than cure#fine"
fi=f.split(" ")

##join

s1 = "".join(fi)
print(s1.split("#"))
planet = "Jupiter"
num_moons = 79
sentence = planet + " has " + str(num_moons) + " Known moons."
print(sentence)
#capitalize
quote = "hello welcome to python trianing"
op = quote.capitalize()
#op = quote.islower()
print(op)

a = "msk"
age = 10
sentence = a + " is of "+str(age)+" years old."
print(sentence)

