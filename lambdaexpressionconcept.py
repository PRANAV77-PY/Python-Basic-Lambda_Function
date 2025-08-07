#without lambda function
def square(s):
    return s * s 


print(square(4))        


#with lambda function
square = lambda s: s * s

print(square(3))

#without klambda function
def arg(a,b):
    return a + b

print(arg(2,3))

#with lamda function
arg = lambda a,b : a + b

print(arg(6,4))
