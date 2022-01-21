# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:19:41 2021

@author: aarthi.reddy.tumu
"""

#class Dog: # class
# num_of_legs = 4 # class variables
# can_fly = False
# num_teeth = 42
#
# def bark(self):
#  return "bow"
#
#
#golden_retriever = Dog() # object creation
#
#print(golden_retriever.bark())



##constructor __init__()
#never return
#class Family:
# def __init__(self,fname,lname,age,relation):#constructor
#  self.fname = fname
#  self.lname = lname
#  self.age = age
#  self.relation = relation
#  
# def fullname(self):
#  return self.fname + " " + self.lname
#
#father = Family("Bob","PArr",45,"father")
#mother = Family("Lily","parr",38,"mother")
#
#
#print(father.age,father.fullname())




#inheritance:
#single inheritance
#multiple inheritance
#multilevel inheritance



#class Person: # Parent class / Base class
# def __init__(self,name,age,gender):
#  self.name = name
#  self.age = age
#  self.gender = gender




#class Teacher(Person): #child class /derived class
#  def __init__(self,name,age,gender,grade,subjects = None):
#  #Person.__init__(self,name,age,gender)
#   super().__init__(name,age,gender)
#   self.grade = grade
#   self.subjects = []
#
#
#
#  def add_subjects(self,new_subject):
#   if new_subject not in self.subjects:
#    self.subjects.append(new_subject)
#    print("Subject added")
#   else:
#    print("subject already exists")
#
#
#
#t1 = Teacher("lily",22,"female",10)
#print(t1.name,t1.gender,t1.add_subjects("Maths"))
#print(t1.subjects)




#class Student(Person):
# def __init__(self,name,age,gender,grade,fee):
#  super().__init__(name,age,gender)
#  self.grade= grade
#  self.fee = fee
#
# def increase_fee(self):
#  self.fee *=1.05
#  return self.fee
##
#s1= Student("bob",12,"male",10,15000)
#print(s1.name,s1.age,s1.gender,s1.increase_fee())
#
#
#
#class Alumni(Student):
# def __init__(self,name,age,gender,grade,fee,grad_year):
#  super().__init__(name,age,gender,grade,fee)
#  self.grad_year = grad_year
#
#
#a1 = Alumni("parr",22,"male",11,12000,2001)
#print(a1.increase_fee())


#Encapsulation
#class BankAccount:
#    def __init__(self,acc_num,acc_name,balance):
#        self.__acc_num = acc_num
#        self.__acc_name = acc_name
#        self.__balance = balance
#    def get_acc_num(self):
#        return self.__acc_num
#    def get_acc_name(self):
#        return self.__acc_name
#    def get_balance(self):
#        return self.__balance
#    def set_acc_num(self,new_acc_num):
#        self.__acc_num = new_acc_num
#    def add_money(self,deposit):
#        self.__balance+=deposit
#        print("amount added")
#    def withdraw(self,withdraw):
#        if self.__balance<withdraw:
#            print("insufficient balance")
#        else:
#            self.balance-=withdraw
#            print("the amount withdrawn")
#acc1= BankAccount(1101,"jeff",100E6)
##acc1.acc_name = "msk"
##print(acc1.acc_name,acc1.acc_num,acc1.balance) - throws error cannot access private without get
##getter functions/accessor
#print(acc1.get_acc_name(),acc1.get_acc_num(),acc1.get_balance())
#
#
#print(acc1.set_acc_num(1102))
#print(acc1.get_acc_num())
#acc1.__balance = 10
#print(acc1.get_balance())
#print(acc1.__balance)
#del acc1.__balance
#
##decalring outside by changing value is not encouragedas shown below ... since, it breaks the concept of encapsulation. Always use set  & get method to initialize and get value
#acc1._BankAccount__balance = 10
#print(acc1.get_balance())
  



##SAME METHOD NAMES BUT DIFFERENT Arg
class Employee:
 def hello_emp(self,empname=None):
  if empname is not None:
   print("Hello"+empname)
  else:
   print("Hello")

emp1 = Employee()

emp1.hello_emp()
emp1.hello_emp("Bob")
class Area:
 def find_area(self,a=None,b=None):
  if a!=None and b!=None:
   print("Area of Rect",(a*b))
  elif a!=None:
   print("area of square",(a*a))
  else:
   print("Nothing")

obj1 =Area()
obj1.find_area()
obj1.find_area(10)
obj1.find_area(10,20)
#Method Overriding
#inheritance
#
class Animal:
    multicellular = True
    def breathe(self):
        print("i breathe oxygen")
    def feed(self):
        print("i eat food")
class Herbi(Animal):
    def feed(self):
        print("i eat only plants, vegan")
h = Herbi()
h.feed()
h.breathe()







