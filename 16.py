a = 2**123-1
numberToCheck = (a)
def checkIfPrime(numberToCheck):
    for x in range(2, numberToCheck):
        if (numberToCheck % x == 0):
            return False,x
print(checkIfPrime(numberToCheck))
