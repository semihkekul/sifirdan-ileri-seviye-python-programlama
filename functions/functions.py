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
print(func1(L2[:]), L2) # copy by address
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