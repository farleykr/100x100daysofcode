# This is what a decorator looks like under the hood.
# The doctest shows how to use it.

"""
>>> @decorator
... def say_hi():
...     print('Hi!')
... 
>>> say_hi()
Your function has been decorated.
Hi!
"""

def decorator(og_func):
    def wrapper():
        print('Your function has been decorated.')
        og_func()
    return wrapper