from math import sqrt, sin

def heron(a, b, c):
    p = (a + b + c)/2
    area = sqrt(p*(p-a)*(p-b)*(p-c))
    return area

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
print(heron(a, b, c))