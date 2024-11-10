#wapp to check the type of the functions
import types
class c:
    def x():
        return 1
    def y():
        return 1
    def b():
        return 2       

print(isinstance(c().x,types.MethodType))
print(isinstance(c().y,types.MethodType))
print(isinstance(c().b,types.MethodType))
print(isinstance(max,types.MethodType))
print(isinstance(abs,types.MethodType))