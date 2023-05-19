# name1='tony'
# # name2='Stark'
# # print(name1,name2)
# # age=51
# # print(age)
# # is_genius=True
# # print(is_genius)
# name=input("what is your name ?")
# print("hello bn"+name)
# old_age=input("Enter your age ?")
# new_age=int(old_age)+5
# print(new_age)
# ------------------------------------------------------------
# first=input("Enter your first number=")
# second=input("enter your 2nd number")
# sum=print("sum of two numbers are  "+str(int(first)+int(second)))
# ------------------------------------------------------------------
# name=("bunty")
# print(name.upper())
# name=("BUNTY")
# print(name.lower())
# name="ramakrushna biswal"
# print(name.find("s"))
# name="Bunty"
# print(name.replace("Bunty","Ram"))
# print(name)
# name="Bunty"
# print(name.replace("Bu","Mo"))
# keyword---------------------------------------------------------------
# name="bunty"
# print("u" in name)
# name="bunty"
# print("x" in name)#................ We can find string and words in between string like this
# name="Ramakrushna biswal"
# print("biswal" in name)
#==============Arithmatic Opretor==================================
# print(10+2)
# print(10-2)
# print(10*2)
# print(10/2)#return type is float
# print(10%3)
# print(10//2)#here output is not return im float////it returns integer value
# print(10**2)#power opretor
# i=4
# i+=2
# print(i)
# i-=4
# print(i)
# i*=5
# print(i)
# ================Comparision opretor ==========================
# print(3<2)
# print(3>2)
# print(3>=2)
# print(3<=2)
# print(3==2)
# print(3!=3)
# print(3!=2)
# ================Logical opretor=====================
# print(3>2 and 4>2)#if both are true it will print true if one is false it print false
# print(2>1 or 2<1)#if one is true it print true nad if both are false it print false
# print(not 3>2)#it return false
# ====================if else statement===================
# Question 1: create a progam to find a person is able to vote or not ?
# ................ANSWER.............................
# age=input("Enter your age")
# if int(age)>=18:
#     print("you are adult")
#     print("you can vote")
# elif int(age)<18 and int(age)>3:
#     print("You are in school")
# else:
#     print("you are a child")
# ===============Mini project to build a calculetor=================!!!!!!!!!!!!!!
# first=input("Enter the first number=")
# opretor=input("Enter the opretor[+,-,*,**,%,/,%]=")
# second=input("Enter the second number=")
# first=int(first)
# second=int(second)
# if opretor=="+":
#     print(first+second)
# elif opretor=="-":
#     print(first-second)
# elif opretor=="*":
#     print(first*second)
# elif opretor=="**":
#     print(first**second)
# elif opretor=="%":
#     print(first%second)
# elif opretor=="/":
#     print(first/second)
# else:
#     print("Opretor is not found")
# ===========================range======================================
# number=range(10)
# print(number)
# ================loop in python===================
# *********while loop************
# i=1
# while i<=10:
#     print(i*"x")#for printing stars
#     i=i+1
# i=1
# while i<=10:
#     print(i)#for printing numbers
#     i+=1
# =============for loop in python======================
# for i in range(10):
#     print(i)# here i is a variable we can use anything instead this[like item.....]
# # another example of for loop
# print("another one")
# for item in range(10):
#     print(item+1)
# ==============list in python==================================
# marks=[45,80,56,"bunty"]
# print(marks)
# #another example
# marks=[45,80,56,"bunty"]
# print(marks[0],marks[3])# with a specific location
# #another type of Example
# marks=[45,80,56,"bunty"]
# print(marks[1:3])#here we defined the range so it display only 80,56
# ===============for loop in lists==============================
# marks=[94,93,96]
# for score in marks:
#     print(score)
# =======================lists in python========================using [ ]
# marks=[98,97,93]
# marks.append(99)#for adding anything in the last index
# print(marks)
# marks=[98,97,93]
# marks.insert(0,99)#for adding anything in the fast index
# print(marks)
# marks=[98,97,93]
# marks.insert(0,99)#for find an elelemnt is exits or not
# print(9 in marks)
# marks=[98,97,93]#for how many elements in the list
# print(len(marks))
# ==========while loop in list=============
# marks=[98,97,93]
# i=0
# while i<len(marks):
#     print(marks[i])
#     i+=1
# ===============for cleaning whole the list==============
# marks=[98,97,93]
# i=0
# while i<len(marks):
#     print(marks[i])
#     i+=1
# marks.clear()
# print(marks)
# ===================break and continue statement======================
# student=['ram','gopal','bunty','monty','uma']
# for i in student:
#     if i=='bunty':
#         break
#     print(i)
# #continue
# print("Another line============")
# student=['ram','gopal','bunty','monty','uma']
# for i in student:
#     if i=='bunty':
#         continue
#     print(i)
# ========================Tuple in python=========================using ( )
#tuple is like of list in tuple we can't change anything<3
#here we use paranthesis() for tuple
# marks=(94.95,98)
# print(marks)
# #Another Example of tuple
# marks=(94,95,84,95,95,95,95,95)
# print(marks.count(95))
# #for which index the element exists
# marks=(94,90,84,95,45,85,95,85)
# print(marks.index(95))
# =====================Set in python=============using { }
# marks={94,95,84,95,95,95,95,95}
# print(marks)
# #for loop in set=========================>>>>>>>>>
# marks={94,95,84,95,95,95,95,95}
# for score in marks:
#     print(score)
# ========================Dictionary in python===================
# marks={"english":95,"phy":98}
# print(marks["phy"])
# marks["chem"]=99#adding some marks in the dictionary.
# print(marks)
# marks['phy']=100#changing tha marks of phisics
# print(marks)
# ====================function in python======================
#inbuild function
#module function Ex[import math,import turtle]
# from math import sqrt
# print(sqrt(16))
# #another style
# import math
# print(dir(math))#gives the output of the function used in [math]
# #selecting all the functions we use * at the end
# from math import*
# print(factorial(3))
#==========user define function==================
# def print_sum(first,second):
#     print(first+second)
# print_sum(1,2)
# #another one
# def sum(first,second=4):
#     print(first+second)
# sum(1)
# ===========================TEH END OF PYTHON BASIC FOR ALL==============================
#THANK YOU.................................@mr_ram_babu__ follow me on insta...........