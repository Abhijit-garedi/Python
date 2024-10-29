#to check wheterh it is import types or not
import types
def a(x):
    yield x
def b(y):
    return y
def add(x,y):
    return x+y 

print(isinstance(a(456),types.GeneratorType))
print(isinstance(b(832),types.GeneratorType))
print(isinstance(add(8,2),types.GeneratorType))