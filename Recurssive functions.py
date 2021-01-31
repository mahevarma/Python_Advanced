# Function calling itself is called a recussive function

import array

x = [1, 2, 3, 4]


def factorial(x):
    if x == 0 or x==1 :
        return 1
    else:
       return x*(factorial(x-1))

print(factorial(5))


def add(args):
    if args ==1 or args ==0 :
        return 1
    else:

        return  args-(add(args-1))

print(add(5))