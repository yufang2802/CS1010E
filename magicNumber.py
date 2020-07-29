def get_magic(num):
	total = 0	
	while (num>0):
		total = total + (num%10)
		num = num // 100
	return (total % 10)

number = input("Enter number ")
print(get_magic(int(number)))
