Subject = int(input("How many subject do you enroll? :"))
ca = 0
sum = 0
for i in range(1,Subject+1):
    print("Subject", i, "credit: ", end="")
    credit = float(input())
    print("Subject",i, "grade: ",end ="")
    grade = input()
    if grade == 'A':
        gr = 4
    if grade == 'B+':
        gr = 3.5
    if grade == 'B':
        gr = 3
    if grade == 'C+':
        gr = 2.5
    if grade == 'C':
        gr = 2
    if grade == 'D+':
        gr = 1.5
    if grade == 'D':
        gr = 1
    elif grade == 'F':
        gr = 0

    gp = gr*credit
    ca = ca+credit
    sum = sum+gp
GPA = sum/ca
print('Total credit = ', ca, "GPA : ", GPA)

