#using recursion

def getFactorial(n):
    if n < 2:
        return 1
    else:
        return n * getFactorial(n-1)

#using iteration (loops)

def getFactorial2(n):
    if n > 2:
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        return factorial

number = int(input("Enter n: "))
print(getFactorial(number))
print(getFactorial2(number))