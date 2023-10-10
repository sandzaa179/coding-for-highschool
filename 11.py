n = int(input("starting number :"))
k = int(input("ending number :"))
new = 0
for i in range(n,k+1):
    new = new+i
print("Sum of numbers form", n, "to", k, " = ", new)
