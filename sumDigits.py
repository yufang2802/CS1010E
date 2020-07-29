def sumDigits(string):
    if string//10 == 0:
        return string
    else:
        return (string%10) + sumDigits(string//10)


string = int(input("Enter string: "))
print(sumDigits(string))