"""
In Python, we can pass a variable number of arguments to a function using special symbols.
There are two special symbols:

Special Symbols Used for passing arguments:-

1.)*args (Non-Keyword Arguments)

2.)**kwargs (Keyword Arguments)

1.) *args

The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function.
It is used to pass a non-key worded, variable-length argument list.

"""


def func(*args):
    for x in args:
        print(x)


func(1, 2, 3, 4, 'Mahesh')


def my_func(arg1, *arg2):
    print("Value of arg1 is ", arg1)
    for x in arg2:
        print("Value of sec argument is ", x)


my_func('Mahesh', 'Varma', 'Sandeep', 'Sandy')

"""
2.)**kwargs
The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list.
We use the name kwargs with the double star.
The reason is because the double star allows us to pass through keyword arguments (and any number of them).

-- Keyword argument python treats it as dictionary
"""


def func(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)


func('Mahesh', 'name1', 'name2', name='varma')
