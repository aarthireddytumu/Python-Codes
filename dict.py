# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 13:11:16 2021

@author: aarthi.reddy.tumu
"""

#dictionary#ordered
#changeable
#does not allow duplicates
#{}
#key and values
dict1 = {"brand":"Ford","model":"Mustang","year":1964}
print(dict1)
print(dict1["year"])
print(dict1.pop("year"))
#d2 = {"one":1,"two":2,"two":3} - throws error bcoz keys cannot be same
#keys
#int,float,str,bool,tuple
#values:
#ny thing
#square bracket method
# get method
#print(dict1["year"])  -   since year is removed it throws an error
print(dict1.get("year"))
#
##keys(),values(),items()
#
print(dict1.keys())
print(dict1.values())
print(dict1.items())
#dict1 & dict1.keys() return the o/p of only keys
for i in dict1:
 print(i)
for i in dict1.keys():
 print(i)
for i in dict1.values():
 print(i)
for i,q in dict1.items():
 print(i,q)
print("year" in dict1)
print("year" not in dict1)
#update or change values#
dict1["year"]=2018
print(dict1)

dict1["color"]="blue"
print(dict1)
#update()
car_dict = {'Ford':["figo","Eco","Aspire"],"Honda":"City","Hyundai":["Verna","Creta"]}
supercars = {"Ford":"Mustang","Bugatti":"Veyron"}
print(car_dict["Ford"][2])

