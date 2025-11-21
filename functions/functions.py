import math
import time

def func():
    '''
    DOCSTRING: return 31
    INPUT: none 
    OUTPUT: int 31
    '''
    return 31

print(type(func))
# <class 'function'>

help(func)
'''
Help on function func in module __main__:

func()
    DOCSTRING: return 31
    INPUT: none
    OUTPUT: int 31
'''

##################  copy by value/reference        #########################

L1 = [1,2,3]
L2 = [5,10,15]
def func1(L: list):
    L[0] = 111

print(func1(L1), L1) # copy by reference
print(func1(L2[:]), L2) # copy by value
# None [111, 2, 3] 
# None [5, 10, 15]    


########################      *params    #####################################

def add(*params):
    return sum((params))

print(add(1,2))
# 3
print(add(1,2,3,4,5))
# 15

########################     **args    #####################################

def displayData(**args):
    print(type(args)) # <class 'dict'>
    for key, value in args.items():
        print(f"{key} -> {value}")

displayData( a= 1, b= 2)
# a -> 1
# b -> 2

########################     **kwargs (keyword args)   ######################
print("########################     **kwargs (keyword args)   ######################")

def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,key1 = "value 1", key2 = 'value 2')    
'''
10
20
(30, 40, 50)
{'key1': 'value 1', 'key2': 'value 2'}
'''

##################  nested #############################
print("##################  nested #############################")
def outer(num1):
    def inner_inc(num):
        return num + 1
    return inner_inc(num1)

print(outer(9))
# 10 

##################  return a function #############################
print("##################  return a function #############################")

def calc_pow(pow):

    def inner(number):
        return number ** pow
    
    return inner

square = calc_pow(2)
cube = calc_pow(3)

print(cube(5))
# 125
################## function as parameter #############################
print("##################  function as parameter  #############################")

def summ(a,b):
    return a + b
def subb(a,b):
    return a - b
def prodd(a,b):
    return a * b
def divv(a,b):
    return a / b

def calculator(f1, f2, f3, f4, oper_name):
    if oper_name == "sum":
        return f1
    elif oper_name == "sub":
        return f2
    elif oper_name == "prod":
        return f3
    elif oper_name == "div":
        return f4        
    

oper = calculator(summ, subb, prodd, divv, "prod")

print(oper(3,4))
# 12

################## decorater function #############################
print("################## decorater function #############################")

def my_decorator(func):
    def wrapper(name):
        print("do something before func")
        func(name)
        print("do other thing after func")
    return wrapper

@my_decorator
def sayHello(name):
    print("hello", name)

sayHello("semih")

'''
do something before func
hello semih
do other thing after func
'''

def timer(func):
    def wrapper(*args):
       start = time.time()
       func(*args) 
       end = time.time()

       print(f"{func.__name__ } took {str(end - start)} seconds")

    return wrapper

@timer
def power(a,b):
    print(math.pow(a,b))

power(2,12)
'''
4096.0
power took 0.0011069774627685547 seconds
'''