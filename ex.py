# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:47:38 2020

@author: Prakash
"""


#************python 2 exercises************
print ("Hello")#ts

print(56+5)

cars=100
spr_cars=20
print(cars)
print("tr ar " ,cars," cars availabl")
print("i d ",spr_cars,"cars")
a = 'prakas'
print(a
      )

# format string python 2####++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print("lts talk abt or %s." %a)

print("i av %d cars and %d spr cars" %(cars,spr_cars))

#error
#print("i av %k cars and %k spr cars" %(cars,spr_cars))

xas = "i lv %r" %10
print(xas)

sar='sar'
x = "i lv %s" %(sar)
print(x)

#error
#sar='sar'
#x = "i lv %d" %(sar)
#print(x)

#displays raw data for debugging
sar='sar'
x = "i lv %r" %(sar)
print(x)

sar='sar'
x = "i lv %r" %'saradv'
print(x)

xas = "i lv %r" %10
print(xas)
sar='sar'
x = "so %r" %(xas)
print(x)

print("." * 10)
a1="p"
a2="r"
a3="a"
a4="k"
print(a1+a2)
print(a3+a4)

Days="Mon\nTue\nWed"

print(Days)
x="%r" %(Days)
print(x)
print("%r" %(Days))

print("i am 5'1\" tall")
print('i am 5\'1" tall')
print("""i am 5'1" tall""")

#age= input("your age")
age=25
print(age)


#exec(open('ex13.py').read())

import sys
from sys import argv

len(sys.argv)

script= argv

print("S",script)
#ex5**********format string
name="Prakash"
print(f"Let's talk about {name}.")

#ex6*********
people = 10
x = f"There r {people} here."
binary = "binary"
do_not = "don't"
y=f"1 knows {binary} and 1 {do_not}"
print(x)
print(y)
print(f"I said: {x}")
