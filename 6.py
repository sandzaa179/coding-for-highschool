weight = int(input("Enter your weight : "))
height_cm = int(input("Enter your height : "))
height_m = height_cm/100
BMI = weight/height_m**2
print("Yout BMI is : ",BMI)
if BMI<10:
    print("You are not Human")
elif BMI<18.5:
    print("Your BMI is thin")
elif BMI>=18.5 and BMI<25:
    print("Your BMI is normal")
elif BMI>=25 and BMI<30:
    print("Your BMI is above the standard")
elif BMI>=30 and BMI<35:
    print("Your BMI is fat")
else:
    print("your BMI is very fat")
