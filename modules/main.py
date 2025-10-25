import a_module

a_module.a_func()
# a_func() of a_module

an_object = a_module.AClass()
an_object.a_func_of_a_class()
# a_func() of a_class

help(a_module)
'''
Help on module a_module:

NAME
    a_module - information about a module

CLASSES
    builtins.object
        AClass

    class AClass(builtins.object)
     |  Methods defined here:
     |
     |  a_func_of_a_class(self)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    a_func()
        information about a_module.a_func()

FILE
    d:\dev\sifirdan-ileri-seviye-python-programlama\modules\a_module.py
'''

help(a_module.a_func)
'''
Help on function a_func in module a_module:

a_func()
    information about a_module.a_func()
'''