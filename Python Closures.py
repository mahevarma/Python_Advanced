"""
Closures
nested function

funtion defined inside other function is called nested function
A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

"""


def outer():
    x = 3

    def inner():
        y = 3
        result = x + y
        return result

    return inner


a = outer()
print(a())

"""
we executed the inner function body outside its scope
this technique is called as closure 
here function 'a' and 'inner' are same function and we are execting function outside its scope.

Closure :
Function object that rememberes values in the enclosing scope even if they are not present in memory

Criteria for creating a closure 
1) Nested function
2) Nested function must refer values in enclosing scope
3) Enclosing function must return the nested function 

Advantages :
1) Can avoid global values
2) data hiding
3) let us implement decorators 
"""
