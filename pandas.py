# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 11:33:46 2021

@author: aarthi.reddy.tumu
"""


#Pandas
#series
#dataframe
#panel
#import pandas as pd
#import numpy as np
##series
#weights = pd.Series(np.random.randint(45,60,size = 30))
#print(weights,type(weights))
#a = pd.Series(["Mercury",4879,3.7,False])
#print(a,type(a))
#print(weights.size)
#print(weights.shape)
#print(weights.min())
#print(weights.max())
#print(weights.mean())
#print(weights.head(-12))
#print(weights[13:28])
#print(weights)
#print(weights.mode())
#print(weights.sort_values(ascending = False))
#print(weights.median())
#print(weights.value_counts())
#
#
#
#print(weights[weights==49])



#Pandas DataFrame
#create Dataframe:#empty df
import pandas as pd
data = [["Alex",10],["Clarke",11]]
data = {"Name":["Tom","Jack","Steve","bob"],"Age":[28,29,32,9]}
df = pd.DataFrame(data,index =['a','b','c','d'])
print(df)
data = [{"a":1,"b":2},{"a":5,"b":10,"c":20}]
df = pd.DataFrame(data)
print(df)
##df from series
d = {"one":pd.Series([1,2,3],index=["a","b","c"]),
 "two":pd.Series([1,2,3,4],index=["a","b","c","d"])}

df = pd.DataFrame(d)
print(df)
df = pd.read_csv(r"C:\Users\aarthi.reddy.tumu\Downloads\test.csv")
print(df.head())
df1 = df[["Team","Age"]]
print(df1.head())
df1 = df[50:101][["Team","Height"]]
print(df1.head())
print(df.iloc[100:110,2:5])

#boolean indexinig
print(df[df["Weight"]>200])
print(df[(df["Weight"]>200) & (df["Height"]>80)])

#Data Manipulation Functions:
print(df.T.head())
import numpy as np
df = pd.DataFrame(np.random.randn(5))
print(df)
df["new"]=pd.Series([1,2,3,4,5])
print(df)
del df["new"]
print(df)

s = pd.Series([2,4,5,6,7,8,9,5])
print(s.describe())

df = df.fillna(1.2345)
print(df)

#grouped_team = df.groupby(by="Team")
#print(grouped_team)
#print(grouped_team.agg(func={"Height":['mean','std'],"Age":"count","Weight":["max","min"]}))

print(pd.__version__)






