def my_decorator(fun): # decorator is a plain python function, which takes in a function as an argument and enhances it by adding extra functionality.
    def enhanced_function(*args, **kwargs):
        return fun() + "world!"
        
    return enhanced_function;# the decorator returns the enhanced function, converting my_function into enhanced_function.

@my_decorator
def my_function():
    return "Hello"

print(my_function())  # whenever a decorated function is called, it actually calls the enhanced_function returned by the decorator.  
# Output: ['Hello, World!']

# why use decorators?
# to persist the single responsibility principle, Every function should have one core responsibility. Decorators help achieve this
# we achieve this separating core functionality from auxiliary features like logging, access control, or caching.

# ex2 - 

# todo : a function which checks whether a number if prime or not
# filter function - a filter function which takes a set of number and filters out the primes from it using the is_prime function.
# a decorator which calulates the time , which it took to execute the filter function.


import time
from datetime import datetime

def time_it(fun):
    def wrapper(*args, **kwargs): # *args and **kwargs inside function definition will pack positional and keyword arguments into tuples(=args) and dictionaries(=kwargs) respectively.
        start_time = time.time()
        ans = fun(*args, **kwargs)
        # here we *args and **kwargs are used to make the decorator generic enough to handle any function signature.
        # *args in a function call will unpack the tuple(args) into positional arguments, while **kwargs will unpack a dictionary into keyword arguments.
        # *kwargs in a function call will unpack a dictionary(kwargs) into keyword arguments.
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return ans
    return wrapper

@time_it # by making time_it a decorator we can time any function we want without changing its core logic. 
def filter_primes(is_prime, arr):
    return list(filter(is_prime, arr))

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True;

arr = list(range(0,10)) # range gets converted to list

prime_nums = filter_primes(is_prime, arr) # filter function returns an array of elements, which gave an output of True via filter function
# print(list(prime_nums))

# note-
# using a decorator is the same as calling the decorator function with the target function as an argument.
# i.e., filter_primes = time_it(filter_primes)
# infact this is exactly what the @ syntax does behind the scenes.




def get_current_datetime(base_func):
    def wrapper(*args , **kwargs):
        print("timed at : ", str(datetime.now()))
        return base_func(*args , **kwargs)

    return wrapper


# ex3- one could stack the decorators as well

@get_current_datetime
@time_it # by making time_it a decorator we can time any function we want without changing its core logic. 
def filter_primes(is_prime, arr):
    # stacking decorators like this is the same as calling get_current_datetime(time_it(filter_primes)), the topmost decorator being applied the last.
    return list(filter(is_prime, arr))

print(filter_primes(is_prime, arr))
