#GPA calculator
subject = int(input("How many subject do you enroll? "))
sum = 0
ca = 0
for i in range(1, subject+1) :
    print("Subject " + str(i) + " credit : ", end = '')
    credit = float(input())
    print("Subject " + str(i) + " grade : ", end = '')
    grade = input()
    Grades = {"A":4, "B+":3.5, "B":3, "C+":2.5, "C":2, "D+":1.5, "D":1, "F":0}
    gr = Grades[grade]
    gp = gr * credit
    ca = ca + credit
    sum = sum + gp
gpa = sum / ca
print("Total credit = " + str(ca) + " GPA = " + str(gpa))
