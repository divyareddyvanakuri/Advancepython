import functools
import time

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

# return_greeting("tony")

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

# def decorator(cls):
#     class NewClass(cls):
#         attr = 100
#         return NewClass
# @decorator
# class X:
#     pass

print(return_greeting.__name__)
print(countdown.__name__)


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]

# For loop to reverse the string
for char in rev_str("hello"):
    print(char)

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def number(nums):
    for num in nums:
        yield num

num = number(fibonacci_numbers(10))
# print(sum(number(fibonacci_numbers(10))))
# print(num)
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))

class DataCamp():
    pass

PythonClass = type('PythonClass', (DataCamp,), {'start_date': 'August 2018', 'instructor': 'John Doe'},() )
print(PythonClass)
print(PythonClass.start_date, PythonClass.instructor)
print(PythonClass)

class MyMeta(type):
    pass

class MyClass(metaclass=MyMeta):
    pass

class MySubclass(MyClass):
    pass

print(type(MyMeta))
print(type(MyClass))
print(type(MySubclass))

a = MyClass()
b = MyClass()

print(a == b)


class A(object): 
    def __new__(cls): 
         print("Creating instance") 
         return super(A, cls).__new__(cls) 
  
    def __init__(self): 
        print("Init is called") 
  
A() 

class A(object): 
    def __new__(cls): 
        print("Creating instance") 
  
    def __init__(self): 
        print("Init is called") 
  
print(A())

class GeeksforGeeks(object): 
    def __str__(self): 
        return "GeeksforGeeks"
          
class Geek(object): 
    def __new__(cls): 
        return GeeksforGeeks() 
          
    def __init__(self): 
        print("Inside init") 
          
print(Geek()) 

# class SingletonMeta(type):
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(SingletonMeta,cls).__call__(*args, **kwargs)
#         return cls._instances[cls]

# class SingletonClass(metaclass=SingletonMeta):
#     pass

# class RegularClass():
#     pass


# x = SingletonClass()
# y = SingletonClass()
# print(x == y)


# x = RegularClass()
# y = RegularClass()
# print(x == y)

# class Meta_1(type):
#     def __call__(cls, *a, **kw):
#         print ("entering Meta_1.__call__()")
#         rv = super(Meta_1, cls).__call__(*a, **kw)
#         print(rv)
#         print ("exiting Meta_1.__call__()")
#         return rv

# class Class_1(object):
#     __metaclass__ = Meta_1
#     def __new__(cls, *a, **kw):
#         print ("entering Class_1.__new__()")
#         rv = super(Class_1, cls).__new__(cls, *a, **kw)
#         print(rv)
#         print ("exiting Class_1.__new__()")
#         return rv

#     def __init__(self, *a, **kw):
#         print ("executing Class_1.__init__()")
#         super(Class_1,self).__init__(*a, **kw)

# c = Class_1()
# d = Class_1()
# print( c == d)

class MyDecorator: 
    def __init__(self, function):
        print("inside init function")
        self.function = function 
        print(self.function)
      
    def __call__(self, *args, **kwargs):
        print("inside calling function")
        result = self.function(*args, **kwargs)
        return result
  
@MyDecorator
def login(name, message): 
    print("{}, {}".format(message, name)) 
  
login("welcome to python programming", "hello") 


