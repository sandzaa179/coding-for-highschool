import math
a = int(input("Enter width : "))
b = int(input("Enter height : "))
h = ((a-b)**2)/((a+b)**2)
print("h = ", h)
pi = 22/7
C = ((pi*(a+b))*(1+((3*h)/(10+(math.sqrt(4-(3*h)))))))
print("C = ", C)
