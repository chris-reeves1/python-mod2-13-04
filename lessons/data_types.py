# Start time: 09.30
# Finish: 16.00

# lunch 12.30-13.30

# am 11.00 pm 15.00 (15 mins)

# Comms: 
# - email
# - webex public/private

# webcams: should be on.

# monday: basic data types + complex data types, vars/misc
# tuesday: iteration/conditional
# Wed: functions
# thurs: classes
# fri: tbc

# monday: testing/linting
# tues: project/crud/sql app. 

# web dev: java, js, python. 
# apps: java, go, swift/kotlin. 
# data science: python
# automation/scripting: python, bash
# gaming: c#, c++
# os: c 
# IOT/edge: python


# interpreted vs compiled 
# high level (readability)
# dynamic vs static 


# simple data types:
# - int: numbers
# - floats: decimals
# - strings: words, paragraphs.
# - bool: true/false, 0/1, something/nothing. 

# variables:

# a = 5 - a reference, "name" for a place in memory.  

# x = 2560
# y = 2560 

# print(x is y) == would be for the value, is checks are they the same object.
#  internation (up to 256/-256) - cant be overidden.
#  caching behaves the same but can overridden. 

# print(id(x))
# print(id(y))

# def func():
#     a = int(str(2560))
#     return a

# def func1():
#     b = int(str(2560))
#     return b

# print(func() is func1()) 

# scope

# print(locals() is globals())

# locals inside functions - are preffered/defualt. 
# function args/outputs used to move data around. 
# globals: avoid for general state. 
# globals good for shared config, constants.
# nested/nonlocal: use sparingly.


# def counter():
#     count = 0

#     def increment():
#         global nonlocal count
#         count += 1 
#         return count

#     return increment()

# x  = counter()
# print(x)
 


# global_var = "this is acessible everywhere"

# def func():
#     local_var = "accessible only within this function"
#     global_var = "will this change or not?"
#     print(local_var)
#     print(global_var)


# func()
# print(global_var)

# design:

# efficiancy: speed, ram/cpu
# scalability: features, users, data
# maintainability: readability, structure, comments/docstrings

# import inspect

# # NOT RETURNED

# # also returned
# # this will be returned
# def example(x: int, y=10):
#     """
#     Description: This is a function that adds toegeather 2 numbers.
#     inputs: x: int repsesnts the first number, y is second number has a default of 10.
#     output: returns an int, sum of x and y. 
#     """
#     return x + y 

# example(5, 10)
# print(inspect.signature(example))
# print(inspect.getdoc(example))
# print(inspect.getcomments(example))
# print(inspect.getsource(example))

# name = input("Enter your name: ") 
# age = int(input("Enter your age: "))

# print("name is " + name + " age is " + str(age))
# print("name is ", name, " age is ", age)
# print(f"name is {name.upper()}, age is {age}")


# pi = 3.14256
# print(f"{pi:.2f}")
# print(f"{name:^20}")
# print(f"{age:0>5}")

# print("Person1:\thello how are you\nperson2:\tgood thanks\n \U0001f600")

# string methods:

# print("hello world".upper())
# print("HELLO WORLD".lower())
# print("hello hello hello hello world".replace("hello", "yo", 1))













