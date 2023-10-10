a = int(input("Enter staring number : "))
b = int(input("Enter ending number : "))
c = 0
def fibonacci1(a,b,c):
    for x in range(a,b+1):
        v = c
        c = a+c
        a = v
    return c
n = fibonacci1(a,b,c)
print(n)

def fibonacci2(N):
    if N<0:
        print("N must be non-negative")
    L = ()
    a,b = 1,1
    while len(L) < N-1:
        a, b = b, a+b
        L.append(a)
        
