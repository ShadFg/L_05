import requests

#print(help(requests))

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def Func():
    pass

func = Func
print(func.__name__)

print(type(Human))

number = 100
print(isinstance(number, Human))
print(isinstance(number, int))
print(issubclass(int, Human))

import inspect

print(inspect.ismodule(Human))
print(inspect.isclass(Human))

sig = inspect.signature(Human)
for parameter in sig.parameters.values():
    print(parameter.name, parameter.default())

import sys

print(sys.executable)
print(sys.version)
print(sys.platform)
print(sys.argv)

import random
print(help(random))
print(type(random.Random))
print(inspect.signature(random.Random))
print(type(random.SystemRandom))
print(inspect.signature(random.SystemRandom))