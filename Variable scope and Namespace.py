# Python Scope
# A variable is only available from inside the region it is created. This is called scope

name = 'John Abraham'


def home():
    name = 'John'
    print(name)


home()
print(name)

"""
What is namespace:
A namespace is a system to have a unique name for each and every object in Python.
An object might be a variable or a method.
Python itself maintains a namespace in the form of a Python dictionary
"""

"""
Local Scope
A variable created inside a function belongs to the local scope of that function,
and can only be used inside that function.
"""


def myfunc():
    x = 300  # Local scope variable
    print(x)


myfunc()

"""Function Inside Function
As explained in the example above, the variable x is not available outside the function,
 but it is available for any function inside the function:"""


def myfunc():
    x = 600

    def myinnerfunc():
        print(x)

    myinnerfunc()


myfunc()

# Global

'''
Global keyword is a keyword that allows a user to modify a variable outside of the current scope.
'''

x = 'Mahesh'


def name():
    global x
    x = "mahe"
    print(x)


name()
print(x)

# Non local scope

name = 'Mahesh verma'


def home():
    name = 'Mahi'

    def friends():
        nonlocal name
        name = 'Mahesh'

    print('The current name is %s' % name)
    friends()
    print('The current name is %s' % name)


home()

print(globals())
print(locals())
