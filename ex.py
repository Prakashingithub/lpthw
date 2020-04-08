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
#age=input("How old?\t")
#height=input("How tall ")
#print(f"so,you are {age} and {height} tall")
#ex13*****argv***************************
from sys import argv
#read the WYSS section for how to run this
#run it like****python ex.py 1st 2nd 3rd****
#script, first, second, third = argv
#print("The script is called:", script)
#print("your first variable is:", first)
#print("second var is:", second)
#print("third variable is:", third)

#ex14*****argv***************************
from sys import argv
#run it like*****python ex.py(scriptname) user_name
#script, user_name = argv
#prompt = '>'

#print(f"Hi {user_name}, i'm the {script} script.")
#print("I'd like to ask you a few questions.")
#print(f"Do you like me {user_name}?")
#likes = input(prompt)

#print(f"where do you live {user_name}?")
#lives = input(prompt)

#print("what kind of computer do you have?")
#computer = input(prompt)

#print(f"""Alright, so you said {likes} about liking me.You live in {lives}.
#Not sure where that is. And you have a {computer} computer. Nice.""")

print("end previous ex14\n")

#ex15******read file
from sys import argv
#simple command*****start
#run as***python ex.py ex.py
# script, filename = argv
# txt = open(filename)

# print(txt.read())
#simple command*****end
#as per exercises****
# script, filename = argv
# txt = open(filename)

# print(f"Here's your file {filename}:")
# print(txt.read())
# print("Type the filename again:")
# file_again = input("> ")
#
# txt_again = open(file_again)
#
# print(txt_again.read())
# print(open(ex.py).read())

print("end previous ex14\n")

#ex16********read and write****
from sys import argv #to run**** python ex.py text.txt

# script,filename=argv
# print(f"to erase {filename}")
####### print("to erase yes, hit CTRL-C (^C).") #not working
####### print("to erase no, hit return.") #not working
####### input("?") #not working
# print("open file")
# target=open(filename,'w') #open file in write mode
# print(target.read())
# print("truncating file")
# target.truncate()
# print("need lines")
# line1=input("line 1: ")
# line2=input("line 2: ")
# line3=input("line 3: ")
#
# print("to write these lines")
#
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
# target.write(f"{line1}+\n+ {line2}+ \n +{line3}+'that\'s right'")
# target.write(f"""\n{line1} {line2} {line3} that\'s right""")
# target.write(f"\n{line1} {line2} {line3}\t-that\'s right")
# target=open(filename,'r')
# print(target.read())
# print("close file")
# target.close()

print("end previous ex16\n")
#ex17*****read , write files*******
from sys import argv
from os.path import exists
#
# script, from_file, to_file = argv
# print(f"copy from {from_file} to {to_file}")
# in_file=open(from_file)
# indata=in_file.read()
#
# print(f"The input file is {len(indata)} bytes long")
#
# print(f"Does the output file exists? {exists(to_file)}")
# print("Ready, hit return to continue, CTRL-C to abort.")
# input()
#
# out_file = open(to_file,'w')
# out_file.write(indata)
#
# print("Alright,all done")
# out_file.close()
# in_file.close()

print("end previous ex17\n")

#ex18******Functions******
#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1}, arg2: {arg2}")

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print(f"arg1:{arg1}, arg2: {arg2}")

#this just takes one argument
def print_one(arg1):

    print(f"arg1: {arg1}")

#this one takes no argument
def print_none():
    print("i got nothing")

print_two("apple","pie")
print_two_again("a","b")
print_one("1")
print_none()

print("end previous ex18\n")
#ex19********Functions , variables*****

def add(x,y):
    print(x+y)

x=986454654
y=1
add(x,y)
add(1,9856)

print("end previous ex19\n")
#ex20********Functions&files********
from sys import argv

# script, input_file=argv
#
# def print_all(f):
#     print(f.read())
#
# def rewind(f):
#     f.seek(0)

# def print_a_line(line_count, f): #add end=" " to skip reading blank line
#     print(line_count, f.readline())
#
# current_file= open(input_file)
# print("print whole file:\n")
# print_all(current_file)
# print("lets rewind\n")
# rewind(current_file)
# print("lets print 3 lines:\n")
# current_line=1
# print_a_line(current_line,current_file)
# current_line=current_line+1
# print_a_line(current_line,current_file)
# #f.readline() --reads a line and moving the read head to right after \n
# current_line=current_line+2
# #it gives the line_count as +2 but reads the line after \n
# print_a_line(current_line,current_file)

print("end previous ex20\n")

#ex21***********Functions***
def add(x,y):
    print(f"adding {x} + {y}")
    return x+y

print(add(5,6))

def sub(x,y):
    return x-y

print(sub(6,9))

print("end previous ex21\n")
#ex22*****# REVIEW:
#ex23*****string,bytes,character encoding
#####run as***-python ex.py utf-8 strict
#####can also test using -ex.py utf-16 strict /ex.py utf-32 strict
#####while using big5 --ex.py big5 strict
####ex.py big5 replace
# import sys
# script, encoding, error = sys.argv
#
#
# def main(language_file,encoding,errors):
#     line = language_file.readline()
#
#     if line:
#         print_line(line,encoding,errors)
#         return main(language_file,encoding,errors)
#
# def print_line(line,encoding,errors):
#     next_lang = line.strip()
#     raw_bytes = next_lang.encode(encoding,errors=errors)
#     cooked_string = raw_bytes.decode(encoding,errors=errors)
#
#     print(raw_bytes, "<===>", cooked_string)
#
# languages = open("languages2.txt", encoding="utf-8")
# ##### languages = open("languages.txt", encoding="ANSI")
# main(languages, encoding, error)

print("end previous ex23\n")
#ex24*****
print("Practice")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """\tThe lovely world \n needs love\n\twhere there is none."""
print("----------")
print(poem)
print("----------")

five=10-2+3-6

print(f"This should be five: {five}")

def secret_formula(started):
    Jelly_beans = started*500
    Jars = Jelly_beans/1000
    return Jelly_beans, Jars

value=10000
beans, jars = secret_formula(value)
#another way to format string
print("With a starting value of: {}".format(value))
print(f"we'd have {beans} beans and {jars} jars.")

value=value/10
formula=secret_formula(value)
print("We'd have {} beans and {} jars.".format(*formula))

print("end previous ex24\n")
#ex25*******
####sentence="All good things come to those who wait"
def break_words(sentence):
    """Function will break_words"""
    words=sentence.split(' ')
    return words

def sort_words(words):
    """sort the words"""
    return sorted(words)

def print_first_word(words):
    """print first word"""
    word=words.pop(0)
    print(word)

def print_last_word(words):
    word=words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """takes full sentence and rturns sorted words"""
    words=break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words=break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words=sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

print("end previous ex25\n")

#ex31*************
# print("""You enter a dark room with two doors.Do you go through door #1 or door #2? """)
# door =input("> ")
# if door=="1":
#     print("There's a giant bear eating a cheese cake.")
#     print("what do you do?")
#     print("1.Take the cake \n 2.Scream at the bear")
#     bear=input("> ")
#     if bear == "1":
#         print("The bear eats you")
#     elif bear == "2":
#         print("The bear eats your leg")
#     else:
#         print(f"Well, doing {bear} is probably better")
#         print("Bear runs away")
# elif door=="2":
#     print("You stare into the endless abyss at Cthulhu's retina.")
#     print("1.Blueberries\n2.Yellow jacket clothespins\n3.Understanding revolvers yelling melodies.")
#     insanity = input("> ")
#     if insanity =="1"or insanity == "2":
#         print("Your body survives powered by a mind of jello.")
#     else:
#         print("The insanity rots your eyes into muck.")
# else:
#     print("Good job!")

print("end previous ex31\n")
##ex32**************for loop******
the_count = [1,2,3,4,5]
fruits = ['apple','orange','banana','mango']
change = [1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
    print(f"This is count {number}")

for fruits in fruits :
    print(f"A fruit type:{fruits}")

for i in change:
    print(f"I got {i}")

elements = []
for x in range(0,6):
    print(f"adding {x} to the list")
    elements.append(x)
print(elements)
for i in elements:
    print(f" element was {i}")

print("end previous ex32\n")

#ex33****while loop*****
i=0
numbers = []

while i<6:
    print(f"At the top i is {i}")
    numbers.append(i)
    print("numbers now:", numbers)
    i = i + 1
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

def while_loop(i):
    numbers = []
    while i<6:
        print(f"At the top i is {i}")
        numbers.append(i)
        print("numbers now:", numbers)
        i = i + 1
        print(f"At the bottom i is {i}")
    print("The numbers: ")
    for num in numbers:
        print(num)

jars = [1,2,3,4,5]

for cakes in jars:
    while_loop(cakes)

print("-----------------------end previous ex33-------------------------\n")

#ex35*********

from sys import exit
#
# def int_test(x):
#     try:
#         int(x)
#         #print("*True*")   #just to check output
#         return True
#     except ValueError:
#         #print("*False*")   #just to check output
#         return False
#
# def gold_room():
#     print("This room is full of gold. How much do you take?")
#     choice = input("> ")
#     if int_test(choice):   #This will execute if the Function returns True
#         print("converting choice as integer.")
#         how_much=int(choice)
#         print(f"{choice}! good, it is a number")
#         if how_much < 50:
#             print("Nice, you are not greedy.")
#             exit(0)
#         else:
#             dead("greedy.")
#     else:
#         print(f"{choice}! Man, type a number.")
#         exit(0)
#
#
# def bear_room():
#     print("Bear here.")
#     print("Bear has a bunch of honey.\nThe fat bear is in front of door.\n")
#     print("How are you going to move the bear?")
#     bear_moved = False
#
#     while True:
#         choice = input("> ")
#         if choice == "take honey":
#             dead("The bear slaps you.")
#         elif choice == "taunt bear" and not bear_moved:
#             print("Bear has moved form the door.")
#             print("You can go through it now.")
#             bear_moved=True
#         elif choice == "taunt bear" and bear_moved:
#             dead("The bear gets pissed off and chews your leg off.")
#         elif choice == "open door" and bear_moved:
#             gold_room()
#         else:
#             print("I got no idea what that means.")
#
# def cthulhu_room():
#     print("Here you see the great evil Cthulhu.")
#     print("He, it, whatever stares at you and you go insane.")
#     print("Do you flee for your life or eat your head?")
#
#     choice = input("> ")
#
#     if "flee" in choice:
#         strart()
#     elif "head" in choice:
#         dead("Well that was tasty!")
#     else:
#         cthulhu_room()
#
# def dead(why):
#     print(why, "Good job!")
#     exit(0)
#
# def start():
#     print("You are in a dark room.")
#     print("There is a door to your right and left.")
#     print("Which one do you take?")
#
#     choice = input("> ")
#
#     if choice == "left":
#         bear_room()
#     elif choice == "right":
#         cthulhu_room()
#     else:
#         dead("You stumble around the room untill you starve.")
#
# start()

print("-----------------------end previous ex35-------------------------\n")

#ex38****************************
ten_things = "apple orange crows telephone light sugar"

print("Wait there are not 10 things. lets fix")

stuff=ten_things.split(' ')  #split using spaces
more_stuff = ["Day", "Night","Song","Frisbee","corn","banana","girl","boy"]

while len(stuff) !=10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There {len(stuff)} items now.")


print("There we go: ", stuff)
print("lets do somethings with stuff.")

print(stuff[1])
print(stuff[-1])  #fancy
print(stuff.pop())
print(' '.join(stuff)) #cool? join with spaces
print('#'.join(stuff[3:5])) #super stellar!

ten_things = "2apple 2orange 2crows 2telephone 2light 2sugar"

print("Wait there are not 10 things. lets fix")

stuff=ten_things.split(' ')  #split using spaces
more_stuff = ["2Day", "2Night","2Song","2Frisbee","2corn","2banana","2girl","2boy"]

for i in stuff:
    i=len(stuff)+1
    if i>10:
        break
    else:
        next_one = more_stuff.pop()
        print("Adding: ", next_one)
        stuff.append(next_one)
        print(f"There {len(stuff)} items now.")

print("There we go: ", stuff)
print("lets do somethings with stuff.")

print(stuff[1])
print(stuff[-1])  #fancy
print(stuff.pop())
print(' '.join(stuff)) #cool? join with spaces
print('#'.join(stuff[3:5])) #super stellar!


print("-----------------------end previous ex38-------------------------\n")

#ex9****************

#creating a mapping of state to abbreviation
states ={'oregon':'OR','florida':'FL','california':'CA','newyork':'NY','michigan':'MI'}

#create a basic set of states and some cities in them
cities={'CA':'San fransisco','MI':'Detroit','FL':'Jacksonville'}

cities['NY']='newyork'
cities['OR']='Portland'

#print out some cities
print('-'*10)
print("NY state has:", cities['NY'])
print("OR state has:",cities['OR'])

#print some states
print('-'*10)
print("Michigan's abbreviation is :",states['michigan'])
print("Florida's abbreviation is:",states['florida'])

#do it by using the state and cities dict
print('-'*10)
print('Michigan has:',cities[states['michigan']])
print('Florida has:',cities[states['florida']])

#print every state abbreviation
print('-'*10)
for state,abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")

for abbrev,city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print('-'*10)
for state,abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-'*10)
#safely get a abbreviation by state that might not be there
state=states.get('texas')
if not state:
    print("Sorry, no texas.")

state=states.get('michigan')  #states['michigan']
if not state:
    print("Sorry, no michigan.")
else:
    print(state)

#get a city with a default value
city=cities.get('TX','Does not exists')
print(f"The city for the state 'TX' is:{city}")

print("-----------------------end previous ex39-------------------------\n")

#ex40*******************
class Song(object):
    """docstring for Song."""

    def __init__(self, lyrics):
        #super(Song, self).__init__()
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday=Song(["Happy Birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])
print(happy_bday)
print("\nlline747")

bulls_on_parade=Song(["They rally around the family",
                        "With pockets full of shells"])
print(bulls_on_parade)
happy_bday.sing_me_a_song()
print("\nline755")
bulls_on_parade.sing_me_a_song()

#test
def song2(x):
    for line in x:
        print(line)

object=["This is testing",
                    "python",
                    "in atom terminal"]
song2(object)
print("\nlin767")
print(object)
print("\nlin769")
print(song2)
print("\nlin771")
for x in object:
    print(x)

#test using examples

class employee():
    pass

emp1=employee()
emp2=employee()

print(emp1)
print(emp2)

## output--
## __main__.employee object at 0xxxxxxxmmmm
## __main__.employee object at 0yyyyyyzzzzz
## two unique instances are Created
print("to test")
class employee():
    """docstring for employee."""

    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@ashokleyland.com'
        self.fullName=first +" "+ last
    def full_name(self):
        return '{} {}'.format(self.first,self.last)

emp1=employee("prakash","m","45000")

print("lin797")
print(emp1.full_name())
print(employee.full_name(emp1))
print(emp1.fullName)
#### print(employee.fullName(emp1)) ##error
print(emp1.email)
print(emp1.last)

print("lin805")

class MyStuff():

    def __init__(self):
        self.tangerine = "And now a thousand years"

    def apple(self):
        print("I am classy apples!")
        print("two")
        print("three")

thing=MyStuff()
print(thing.tangerine)
print(thing.apple())
print('lin820')
print(MyStuff.apple(thing))
### print(MyStuff.tangerine(thing)) #not working


print("-----------------------end previous ex40-------------------------\n")

#ex41**************

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"

WORDS = []

PHRASES = {"class%%%(%%%):":"Make a class named %%% that is-a %%%.",
            "class%%%(object):\n\tdef__init__(self,***):":"class %%% has-a __init__ that takes self and *** params",
            "class %%%(object)\n\tdef***(self,@@@):":"class %%% has-a function *** that takes self and @@@ params",
            "*** = %%%()":"set *** to an instance of class %%%.",
            "***.***(@@@)":"from *** get the *** function, call it with params self, @@@",
            "***.***='***'":"from *** get the *** attribute and set it to '***'."}

#do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

#load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(),encoding="utf-8"))

def convert(snippet,phrase):
    class_names=[w.capitalize() for w in random.sample(WORDS,snippet.count("%%%"))]
    other_names=random.sample(WORDS,snippet.count("***"))
    results=[]
    param_names=[]
    for i in range(0,snippet.count("@@@")):
        param_count=random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS,param_count)))
    for sentence in snippet,phrase:
        result=sentence[:]
        #fake class name
        for word in class_names:
            result.replace("%%%",word,1)
        #fake other names
        for word in other_names:
            result.replace("***",word,1)
        #fake params list
        for word in param_names:
            result.replace("@@@",word,1)
        results.append(result)
    return results

#keep going untill they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)
        for snippet in snippets:
            phrase=PHRASES[snippet]
            question,answer=convert(snippet,phrase)
            if PHRASE_FIRST:question,answer=answer,question
            print(question)
            input("< ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
