import math
a = int(input("a = "))
b = int(input("b = "))
def plus(a,b):
    x = a+b
    return x
d = plus(a,b)
print(a, "+", b, "=", d)

def minus(a,b):
    x = a-b
    return x
d = minus(a,b)
print(a, "-", b, "=", d)

def division(a,d):
    if b != 0:
        x = a/b
        print(a, "/", b, "=", d)
        return x
    else:
        print("division must not be equal to 0")
d = division(a,b)

c = int(input("c = "))
def sqrtx(a,b,c):
    if b != 0:
        x_plus = (-b+(math.sqrt((b**2)-(4*a*c))))/(2*a)
        x_minus = (-b-(math.sqrt((b**2)-(4*a*c))))/(2*a)
        print("x1", "=", x_plus,",","x2", "=", x_minus)
        return x_plus,x_minus
    else:
        print("b must not 0")
x1,x2 = sqrtx(a,b,c)
