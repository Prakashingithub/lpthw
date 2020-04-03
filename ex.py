# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:47:38 2020

@author: Prakash
"""

#path*******C:\Users\Prakash\github\lpthw

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

# format string python 2####++++++++++++++++++++++++++++++++++++++++++++++++
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
print(f"I also said :'{y}'")
hilarious=False
joke_valuation="isn't that joke so funny?!{}"
print(joke_valuation.format(hilarious))
w = "this is 1 \n "
r="this is 2"
print(w+r)
#ex7***************more printing**********
print("My child's legs are white as {}".format("snow"))

print("end 7")
#ex8********** string formatting********
formatter = "{} {} {} {}"
print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,True,True))
print(formatter.format(formatter,formatter,formatter,formatter))

print("end 8\n")

#ex9*********
Days="Mon\nTue\nWed"
print(Days)
print("""Hidog""")
print("end previous ex\n")
#ex10************escape sequences****
print("i am 5'1\" tall")
print('i am 5\'1" tall')
print("""i am 5'1" tall""")
print("end previous ex\n")
#ex11************taking input*******
#end=' '***tell print to not end the line with a newline character
print("How old?",end=' ')
#age=input()
print("How tall?",end=' ')
#height=input()
#print(f"so,you are {age} old and {height} tall")
#print("end previous ex\n")
#int(input())*******get number as string and converts to int
#ex12**********
print("\n ex 11")
age=input("How old?\t")
height=input("How tall ")
print(f"so,you are {age} and {height} tall")
