score = float(input("Enter your score : "))
if score > 100 or score < 0:
    print("Score must be 0-100")
elif score >= 80:
    print("You get A")
elif score >= 70 and score < 80:
    print("You get B")
elif score >= 60 and score < 70:
    print("You get C")
elif score >= 50 and score < 60:
    print("You get D")
else:
    print("You get F")
