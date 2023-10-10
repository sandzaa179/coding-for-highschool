number = int(input("Enter nuber of factorial : "))
print(number,"!", "=", end='')
fac = 1
for i in range(1,number+1):
    fac = fac*i
print(fac)
    
